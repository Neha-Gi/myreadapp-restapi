from django.urls import path
from . import views

app_name = 'book-urls'
urlpatterns = [
    path("author/",views.list_authors,name='list_authors'),
    path('tag/',views.list_tags,name='list_tags'),
   # path('book/',views.create)
]
