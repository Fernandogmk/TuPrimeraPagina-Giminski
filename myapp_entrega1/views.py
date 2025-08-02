from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Hola, mundo!"}
    return render(request, 'myapp_entrega1/index.html', context)