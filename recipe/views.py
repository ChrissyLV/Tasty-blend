from django.shortcuts import render

# Create your views here.

def home_page(request):
    " home_page view"

    return render(request,'index.html')