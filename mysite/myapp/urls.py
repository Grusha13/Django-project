from django.urls import path

from . import views
# URL request as parameter and return an HTTP response or throw an exception like 404
urlpatterns = [
    path('',views.index,name='index'),
    path('book/<int:book_id>', views.book_by_id, name='book_by_id'),
]
