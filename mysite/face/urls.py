from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("contact/", views.contact, name='contact'),
    path("shorten_link/", views.shorten_link, name='shorten_link'),
    path('shorten/', views.shorten, name='shorten'),
    path('shorten/<str:short_link>/', views.redirect_to_original, name='redirect_to_original'),
]
