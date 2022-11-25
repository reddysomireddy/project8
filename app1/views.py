from django.shortcuts import render

# Create your views here.
def a1_forloop(request):
    d={'a':200,'b':100}
    return render(request,'a1_forloop.html',d)
def a1_forloop2(request):
    d={'a':300,'b':250}
    return render(request,'a1_forloop2.html',d)