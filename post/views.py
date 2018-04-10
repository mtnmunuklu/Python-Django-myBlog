from django.shortcuts import render,HttpResponse

# Create your views here.

def post_index(request):
    return HttpResponse('Burası Post index sayfası')

def post_detail(request):
    return HttpResponse('Burası Post detail sayfası')

def post_create(request):
    return HttpResponse('Burası Post create sayfası')

def post_update(request):
    return HttpResponse('Burası Post update sayfası')

def post_delete(request):
    return HttpResponse('Burası Post delete sayfası')