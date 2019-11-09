from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password2'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('artwork'))
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)
