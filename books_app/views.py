from django.shortcuts import render, HttpResponse, redirect
from .models import *


# HTML CONTEXTS 

def splash(request):
    return render(request, "splash.html")

def index(request):
    
    context = {
        
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }
    
    return render(request, "index.html", context)


def authors_index(request):
    
    context = {
        
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }
    
    return render(request, "authors_index.html", context)

 

# ADD A BOOK

def add_book(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc'],
    )
    return redirect('/books_page')

# ADD AN AUTHOR

def new_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes'],
    )
    return redirect('/authors_page')



# DELETE A BOOK 

def delete_book(request, book_id):
    del_book = Book.objects.get(id=book_id)
    del_book.delete()
    return redirect('/books_page')



# ADD AUTHOR TO BOOK 

def add_author(request, book_id):
    author = Author.objects.get(id=request.POST["add_author"])
    book = Book.objects.get(id=book_id)
    book.authors.add(author)
        
    
    return redirect(f'/view_book/{book_id}')


# ADD BOOK TO AUTHOR

def new_book(request, author_id):
    book = Book.objects.get(id=request.POST["new_book"])
    author = Author.objects.get(id=author_id)
    author.books.add(book)
        
    
    return redirect(f'/view_author/{author_id}')


# DELETE AUTHOR FROM BOOK

def delete_author(request, book_id):
    author = Author.objects.get(id=request.POST["delete_author"])
    author.delete()
        
    
    return redirect(f'/view_book/{book_id}')


# DELETE BOOK FROM AUTHOR

def remove_book(request, author_id):
    book = Book.objects.get(id=request.POST["remove_book"])
    book.delete()
        
    
    return redirect(f'/view_author/{author_id}')


# VIEW BOOK

def view_book(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id),
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
        
    }
    return render(request,"books.html", context)


# VIEW AUTHOR

def view_author(request, author_id):
    context = {
        "author": Author.objects.get(id=author_id),
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
        
    }
    return render(request,"authors.html", context)







