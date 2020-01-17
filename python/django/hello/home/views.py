from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Hello World!") 

def aboutPage(request):
    return HttpResponse("About Page")