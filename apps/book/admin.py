from django.contrib import admin
from .models import Author,Book,Tag,BookAuthor



# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(BookAuthor)