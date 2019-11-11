from django.urls import path
from . import views


# Creating the urlpatterns for displaying the artwork.
urlpatterns = [
    path('', views.all_artwork, name='all_artwork'),
    path('artwork_detail', views.artwork_detail, name='artwork_detail'),
    path('artwork_like', views.artwork_like, name='artwork_like')
]