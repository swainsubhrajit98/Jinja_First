from django.shortcuts import render

# Create your views here.
def Jinja(request):
    return render(request,'Jinja.html',context={'name':'Subhrajit','age' : 2})