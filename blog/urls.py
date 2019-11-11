from django.urls import path
from . import views


# creating the blog url
urlpatterns = [
    path('blog/', views.blog, name='all_blogs')

]