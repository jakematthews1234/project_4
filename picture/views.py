from django.shortcuts import render, HttpResponseRedirect
from .models import Artwork, Comment, Like
from .form import Comment_Form
import stripe


def all_artwork(request):
    """ Creating the options for artwork, being sold or not sold. """
    all_unsold = Artwork.objects.filter(status=Artwork.FOR_SALE).order_by('-likes')
    all_sold = Artwork.objects.filter(status=Artwork.SOLD)

    """ Creating the likes dictionary """
    likes_dictionary = {}
    if request.user:
        likes = Like.objects.all()
        for like in likes:
            likes_dictionary[like.artwork_id] = True
    return render(request, 'picture/all_artwork.html',
                  {'artwork_sale': all_unsold, 'artwork_sold': all_sold,
                   'likes': likes_dictionary})


def artwork_like(request):
    """ Creating the view that allows users to like a piece of individual artwork by grabbing the unique
    'id' from the database and saving the like to that piece of artwork. """
    artwork_number = request.GET.get('id')
    following_page = 'artwork_detail?id='+str(artwork_number)
    if 'following' in request.GET:
        following_page = request.GET.get('following')
    artwork = Artwork.objects.get(id=artwork_number)
    user = request.user
    like = Like(user=user, artwork=artwork)
    """ Save the like in the database, attached to the correct artwork piece using its unique ID """
    like.save()
    return HttpResponseRedirect(following_page)


def artwork_detail(request):
    """ View that grabs the artwork and its unique id's; allowing users to leave a comment on any artwork within
     the database. """
    artwork = Artwork.objects.get(id=request.GET.get('id'))
    print(artwork)
    """ Import the Comment_form from models  """
    form = Comment_Form()
    try:
        like = Like.objects.get(artwork=artwork, user=request.user)
    except Like.DoesNotExist:
        like = None
    if 'comment' in request.POST:
        comment = request.POST.get('comment')
        comment = Comment(user=request.user, artwork=artwork, comment=comment)
        comment.save()

    comments_already_recieved = Comment.objects.filter(artwork=artwork)

    is_liked = False
    if like:
        is_liked = True
    return render(request, 'picture/artwork_detail.html', {'artwork': artwork,
                                                            'liked': is_liked,
                                                            'form': form,
                                                            'comment': comments_already_recieved})

# Set your secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys


stripe.api_key = ''

session = stripe.checkout.Session.create(
  payment_method_types=['card'],
  line_items=[{
    'name': 'artwork',
    'description': 'an original piece of artwork',
    'amount': 500,
    'currency': 'gbp',
    'quantity': 1,
  }],
  success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
  cancel_url='https://example.com/cancel',
)