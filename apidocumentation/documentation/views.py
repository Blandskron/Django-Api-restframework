from django.shortcuts import render

def api_documentation_view(request):
    return render(request, 'documentation/api_documentation.html')

def create_person_view(request):
    return render(request, 'documentation/create_person.html')

def read_persons_view(request):
    return render(request, 'documentation/read_persons.html')

def update_person_view(request):
    return render(request, 'documentation/update_person.html')

def delete_person_view(request):
    return render(request, 'documentation/delete_person.html')

def obtener_lista_personas(request):
    return render(request, 'documentation/obtener_lista_personas.html')

def crear_persona(request):
    return render(request, 'documentation/crear_persona.html')

def obtener_detalles_persona(request):
    return render(request, 'documentation/obtener_detalles_persona.html')

def actualizar_persona(request):
    return render(request, 'documentation/actualizar_persona.html')

def eliminar_persona(request):
    return render(request, 'documentation/eliminar_persona.html')

def inicio(request):
    return render(request, 'documentation/inicio.html')