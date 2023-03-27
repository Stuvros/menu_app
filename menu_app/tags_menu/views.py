from django.shortcuts import render

def home(request):
    return render(request, 'tags_menu\home.html')

def test(request):
    pass