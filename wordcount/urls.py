from django.urls import path
from . import page1
urlpatterns = [
    path('', page1.homepage , name='home'),
    path('count' , page1.count ,name='count'),
    path('about', page1.about  , name='about'),    
]
