from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('book_detail/<slug:slug>/', views.book_detail, name = 'book-detail')    
]
