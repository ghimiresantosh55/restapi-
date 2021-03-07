from django.contrib import admin
from django.urls import path, include
# from.import views
from .views import article_list

urlpatterns = [
    # path("index",views.index,name="index"),
    # path("practice/<str:name>",views.greet,name=""),  
    # path("santosh",views.santosh,name="santosh"),
    path('article/', article_list, name="article")
    
]
