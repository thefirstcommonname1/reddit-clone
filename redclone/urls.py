from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id_param>/', views.listing, name="listing"),
    path('upvote/<int:id_param>/', views.upvote, name="upvote"),
    path('downvote/<int:id_param>/', views.downvote, name="downvote")
]
