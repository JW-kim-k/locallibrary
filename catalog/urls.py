from django.urls import path
from . import views

app_name="catalog"

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name ='books'),
    path('book/<int:pk>', views.book_detail_view, name='book-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('allBorrowed/', views.allBorrowed, name='allBorrowed'),
    path('book/<uuid:pk>/renwe/', views.renew_book_librarian, name='renew-book-librarian'),
]


urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]