from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('picture.urls')),
    path('blog/', include('blog.urls')),
    path('picture/', include('picture.urls')),
    path('user/', include('user.urls')),
]
