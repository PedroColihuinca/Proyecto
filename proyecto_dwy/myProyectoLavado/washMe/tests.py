from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from .models import Insumos


# Create your tests here.

class TestUsuario(unittest.TestCase):

    def test_grabar_usuario(self):
        valor = 0
        try:
            nombre ="Yohan"
            apellido = "Zuñiga"
            email = "yoh.zu@gmail.com"
            usuario = "Yohanz"
            pass1 = "123123123"
            pass2 = "123123123"

            if pass1!=pass2:
                valor = 0

            else:

                usu = User()

                usu.first_name = nombre
                usu.last_name = apellido
                usu.email = email
                usu.username = usuario
                usu.set_password(pass1)

                usu.save()
                valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

    def test_borrar_usuario(self):
        valor = 0
        usuario ="Yohanz"

        try:
            usu = User.objects.get(username=usuario)
            usu.delete()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

class TestInsumo(unittest.TestCase):
    def test_grabar_insumo(self):
        valor = 0
        try:
            insumo = Insumos(
                nombre="aaaa",
                descripcion="asdASDasda",
                precio=600,
                stock=4
            )
            insumo.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

    def test_borrar_insumo(self):
        valor = 0
        id ="aaaa"

        try:
            insumo = Insumos.objects.get(nombre=id)
            insumo.delete()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

if __name__ == "__main__":
    unittest.main()