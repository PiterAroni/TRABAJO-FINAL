from django.shortcuts import render, HttpResponse
# Create your views here.
def home(request):
    return render(request, "myapp/home.html")

def actividades(request):
    return render(request,"myapp/actividades.html")

def seguimiento(request):
    return render(request, "myapp/seguimiento.html")


