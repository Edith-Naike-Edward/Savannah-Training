from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('posts/', include('posts.urls')),
    path("", views.posts_list, name="posts_list"),
]


