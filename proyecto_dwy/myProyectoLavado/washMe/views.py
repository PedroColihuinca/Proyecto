from django.shortcuts import render
from .models import SliderGaleria,SliderIndex,Insumos,MisionVision

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_autent
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.

def index(request):
    slider = SliderIndex.objects.all()
    return render(request,'web/index.html',{'imagenes':slider})

def galeria(request):
    slider = SliderGaleria.objects.all()
    return render(request,'web/galeria.html',{'imagenes':slider})

def quienes_somos(request):
    lista = MisionVision.objects.all()
    return render(request,'web/quienes_somos.html',{'lista':lista})

def servicios(request):
    return render(request,'web/servicios.html')

def ubicacion(request):
    return render(request,'web/ubicacion.html')



# LOGIN
def login(request):
    if request.POST:
        usuario = request.POST.get("txtNombreusuario")
        contrasenia = request.POST.get("txtPassLogin")

        user1 = authenticate(request,username=usuario, password=contrasenia)

        if user1 is not None and user1.is_active:
            login_autent(request,user1)
            slider = SliderIndex.objects.all()
            return render(request,'web/index.html',{'imagenes':slider})
        else:
            return render(request,'web/login.html',{'msg':'usuario no existe'})
    return render(request,'web/login.html')

# Cerrar sesion
def cerrarSesion(request):
    logout(request)
    slider = SliderIndex.objects.all()
    return render(request,'web/index.html',{'imagenes':slider})




# Agregar usuarios
def formulario(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtapellido")
        email = request.POST.get("txtEmail")
        usuario = request.POST.get("txtNombreusuario")
        pass1 = request.POST.get("txtPass1")
        pass2 = request.POST.get("txtPass2")

        if pass1!=pass2:
            return render(request,'web/formulario.html',{'msg':'Contraseñas diferentes'})

        try:
            usu = User.objects.get(username=usuario)
            return render(request,'web/formulario.html',{'msg':'Este usuario ya existe'})

        except:
            usu = User()

            usu.first_name = nombre
            usu.last_name = apellido
            usu.email = email
            usu.username = usuario
            usu.set_password(pass1)

            usu.save()

            usu = authenticate(request,username=usuario, password=pass1)
            login_autent(request,usu)
            slider = SliderIndex.objects.all()
            return render(request,'web/index.html',{'imagenes':slider})

    return render(request,'web/formulario.html')



# INSUMOS

#Agregar
@login_required(login_url='/login/')
@permission_required('washMe.add_insumos',login_url='/login/')
def formulario_insumo(request):

    if request.POST:
        nombre = request.POST.get("txtnombre")
        stock = request.POST.get("txtStock")
        precio = request.POST.get("txtprecio")
        descripcion = request.POST.get("txtdescripcion")

        insumo = Insumos(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock )
        insumo.save()
        return render(request,'web/formulario_insumo.html',{'msg':'Insumo Guardado'})

    return render(request,'web/formulario_insumo.html')


#Listar
@login_required(login_url='/login/')
@permission_required('washMe.view_insumos',login_url='/login/')
def listar_insumos(request):
    listar = Insumos.objects.all()
    return render(request,'web/formulario_insumo_listar.html',{'listar_insumos':listar})

#Eliminar

@login_required(login_url='/login/')
@permission_required('washMe.add_insumos',login_url='/login/')
@permission_required('washMe.view_insumos',login_url='/login/')
@permission_required('washMe.delete_insumos',login_url='/login/')
def eliminar_insumo(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg='insumo eliminado'
    except:
        msg= 'insumo no eliminado'

    lista = Insumos.objects.all()
    return render(request,'web/formulario_insumo_listar.html',{'lista_insumos':lista,'msg':msg})

#buscar
@login_required(login_url='/login/')
def buscar_insumo(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'web/formulario_insumo_mod.html',{'insumo':insumo})

    except:
        msg = 'NO EXISTE INSUMO'
        
    lista = Insumos.objects.all()
    return render(request,'web/formulario_insumo_listar.html',{'lista_insumos':lista,'msg':msg})

#Modificar

@login_required(login_url='/login/')
@permission_required('washMe.add_insumos',login_url='/login/')
@permission_required('washMe.view_insumos',login_url='/login/')
@permission_required('washMe.change_insumos',login_url='/login/')
def modificar_insumo(request):
    if request.POST:
        nombre = request.POST.get("txtnombre")
        stock = request.POST.get("txtStock")
        precio = request.POST.get("txtprecio")
        descripcion = request.POST.get("txtdescripcion")

        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descripcion
            insumo.stock = stock
            insumo.save()
            msg = 'insumo modificado'
        
        except:
            msg = 'insumo no modificado'

        lista = Insumos.objects.all()
        return render(request,'web/formulario_insumo_listar.html',{'lista_insumos':lista,'msg':msg})
