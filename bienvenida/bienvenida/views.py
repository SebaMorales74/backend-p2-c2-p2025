from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola mundo desde Django")

def mostrar_bienvenida(request):
    tu_nombre = "Sebastian Morales"
    return HttpResponse(f"¡Bienvenidos a mi primera app Django, {tu_nombre}!")