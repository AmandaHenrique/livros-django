from django.shortcuts import render

#Renderiza a parte visual

def home(request):
    return render(request, 'main.html')