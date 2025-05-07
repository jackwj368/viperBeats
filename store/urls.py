from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('favorites/', views.favorites, name='favorites'),
    path('mood/<str:mood>/', views.shop_by_mood, name='shop_by_mood'),
    path('genre/<str:genre>/', views.shop_by_genre, name='shop_by_genre'),
    path('signup/', views.signup, name='signup'),
]