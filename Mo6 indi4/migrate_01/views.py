from django.shortcuts import render
from .models import Departamento,Asignatura,Profesor,Alumno,Transportista
# Create your views here.

def asignaturax(request):
    departamento = Departamento.objects.create(
        nombre='filosofia'
    )
    Departamento.objects.values()
    departamento.save()
    for i in range(0,5):
        asignatura = Asignatura(nombre= 'Walter',
        descripcion = 'walter es muy pesaito',
        )    
    asignatura.save()
    asignatura = Asignatura.objects.values()
    context = {'asig': asignatura}    
    return render(request, 'migrate_01/asignatura.html', context)


def profesorx(request):
    for i in range(0,5):
        profe = Profesor(nombre= 'Claudio',
        apellido = 'Caniullan',
        escuela = 'Manuel de salas',
        fecha_de_contratacion = '2017-02-28',
        sueldo = 1100000
        )
    profe.save()
    profe = Profesor.objects.values()
    context = {'profe': profe}
    return render(request, 'migrate_01/profesor.html', context)


def mostrar_alumnos(request):
    listar_alumnos = list(Alumno.objects.all())
    context = {'alumnos':listar_alumnos}
    return render(request,'migrate_01/alumno.html', context= context)



