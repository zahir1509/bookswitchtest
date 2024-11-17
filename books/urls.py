from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path('', views.home, name='home'),
    path('add-books/', views.add_books, name='add_books'),
    path('view-books/', views.view_books, name='view_books'),
    path('rent-book/<int:book_id>/',views.rent_book, name='rent_book'),
]