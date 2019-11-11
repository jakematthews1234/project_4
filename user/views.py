from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """ The view for users to register an account. """
    if request.method == 'POST':
        """ Import the Django built in UserCreationForm """
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            """ If the register form is filled in correctly, save the new user to the database """
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password2'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('artwork'))
    else:
        """ If the user did not fill out the registration form correctly, redirect them back to the form
        to try again. """
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)
