from django.urls import path
from .views import HomePageView, AboutPageView, ProfilePageView, UserListPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('profile/<uuid:pk>/', ProfilePageView.as_view(), name='profile'),
]

