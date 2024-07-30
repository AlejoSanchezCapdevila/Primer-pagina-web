from django.shortcuts import render




# Create your views here.
def inicio(request):
    return render(request, "App1/index.html")
def profesor(request):
    return render(request, "App1/profesor.html")
def cursos(request):
    return render(request, "App1/cursos.html")
def estudiantes(request):
    return render(request, "App1/estudiantes.html")
def entregas(request):
    return render(request, "App1/entregas.html")