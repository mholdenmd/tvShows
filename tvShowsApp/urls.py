from django.urls import path     
from . import views

urlpatterns = [
    path("shows", views.first),
    path('shows/new', views.index),	
    path('shows/create', views.newShow),
    path("shows/<int:theShowID>", views.TvShowinfomation),
    path('shows/<int:theShowID>/edit', views.EditShow),
    path('shows/<int:theShowID>/update', views.updatedCheese),
    path('shows/<int:theShowID>/destory', views.completedestrution)
]