from django.shortcuts import render

def muro(request):
    return render(request, 'notas/muro.html', {})
