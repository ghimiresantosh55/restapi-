from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Article
from django.views.decorators.csrf import csrf_exempt
from .serializers import Articleserializer

# Create your views here.
@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = Articleserializer(articles,many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) 
        serializer = Articleserializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)    

       

# def index(request):
#     return render(request,"hello/index.html")

# def santosh(request):
#     return HttpResponse("my name is santosh ghimire")

# def greet(request, name):
#     return render(request,"hello/greet.html",{
#        "name":name.capitalize()

#     })
