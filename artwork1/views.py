from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils import timezone
from .models import Artwork, Comment, Like
from .form import Comment_Form


def all_artwork(request):
    all_unsold = Artwork.objects.filter(status=Artwork.FOR_SALE).order_by('-likes')
    all_sold = Artwork.objects.filter(status=Artwork.SOLD)

    likes_dictionary = {}
    if request.user:
        likes = Like.objects.filter(user=request.user)
        for like in likes:
            likes_dictionary[like.artwork_id] = True
    return render(request, 'artwork1/all_artwork.html',
                  {'artwork_sale': all_unsold, 'artwork_sold': all_sold,
                   'likes': likes_dictionary})


def artwork_like(request):
    artwork_number = request.GET.get('id')
    following_page = 'artwork_detail?id='+str(artwork_number)
    if 'following' in request.GET:
        following_page = request.GET.get('following')
    artwork = Artwork.objects.get(id=artwork_number)
    user = request.user
    like = Like(user=user, artwork=artwork)
    like.save()
    return HttpResponseRedirect(following_page)


def artwork_detail(request):
    artwork = Artwork.objects.get(id=request.GET.get('id'))
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
    return render(request, 'artwork1/artwork_detail.html', {'artwork': artwork,
                                                            'liked': is_liked,
                                                            'form': form,
                                                            'comment': comments_already_recieved})
