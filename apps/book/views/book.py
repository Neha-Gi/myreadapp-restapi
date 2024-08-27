from django.db import transaction 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Book,Author
from  apps.book.serializers import ReadBookSerializer,CreateBookSerializer


# Function-base view
@api_view(["GET"])  # by default , it uses a 'GET' method
def list_books(request):
    # Get all authors using ORM
    books = Book.objects.all()

    # Deserialize using the AuthorSerializer
    data = ReadBookSralizer(books, many=True)

    return Response(data.data, status=status.HTTP_200_OK)


# Function-base view
@api_view(["POST"])  # by default , it uses a 'GET' method
def create_book(request):
    with transaction.atomic():
        data = request.data
        authors = data['authors']
        book = CreateBookSerializer(data=data)

        if book.is_valid():
            saved_book = book.save()

            for author in authors:
                author_obj = Author.objects.get(pk=author['id'])
                saved_book.authors.add(author_obj,through_defaults={'role':author['role']})
        

    return Response({'isbn':saved_book.isbn},status=status.HTTP_201_CREATED)

   #return Response({'detail:'Invalid request data','error':'invalid'}, status=status.HTTP_200_OK)
