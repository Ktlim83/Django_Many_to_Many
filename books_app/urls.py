from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash),
    path('books_page', views.index),
    path('authors_page', views.authors_index),
    path('add_book', views.add_book),
    path('add_author/<int:book_id>', views.add_author),
    path('new_author', views.new_author),
    path('new_book/<int:author_id>', views.new_book),
    path('delete_book', views.delete_book),
    path('delete_author/<int:book_id>', views.delete_author),
    path('delete_book/<int:book_id>', views.delete_book),
    path('remove_book/<int:author_id>', views.remove_book),
    path('view_book/<int:book_id>', views.view_book),
    path('view_author/<int:author_id>', views.view_author),
    
    
]