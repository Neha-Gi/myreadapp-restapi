from django.urls import path
from . import views

app_name = 'reader-urls'
urlpatterns = [
    path('login/',views.LogIn.as_view(),name='reader-login')
]