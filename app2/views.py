from django.shortcuts import render

# Create your views here.
def whileloop1(request):
    d={'a':500,'b':400,'c':500}
    return render(request,'whileloop1.html',d)
def whileloop2(request):
    d={'name':'somireddy'}
    return render(request,'whileloop2.html',d)