from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg,Max,Min

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("rating") # this is a query set
    number_of_books = books.count()
    average_rating = books.aggregate( #used to get multiple values from the database
        Avg('rating'),
        Max('rating'),
        Min('rating'))
    
    max_rating = books.aggregate(Max('rating'))
    
    return render(request, 'book_outlet/index.html', {
        'books': books,
        "average_rating": average_rating,
        

    })


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug) # use this shortcut instead of the objects.get method and also the try except block
 
    # try:
    #     book = Book.objects.get(pk=id) # pk is primary key
    # except:
    #     raise Http404()
     
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'rating': book.rating,
        'author': book.author,
        'is_best_selling': book.is_best_selling
    })