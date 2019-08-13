from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')

def equipoDocente(request):
	return render(request, 'miapp/equipoDocente.html')

def libre(request):
	return render(request, 'miapp/libre.html')