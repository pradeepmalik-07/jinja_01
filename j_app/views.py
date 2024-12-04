from django.shortcuts import render

# Create your views here.


def jinj(request):
    d={'name':'pradeep','age':23,'degree':'MCA'} 
    return render(request,'jin.html',context=d)