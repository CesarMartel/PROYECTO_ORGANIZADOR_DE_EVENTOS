# myapp/tests.py
from django.test import TestCase
from .models import Evento # Importa tu modelo Evento desde models.py

class EventoModelTest(TestCase):
    def test_create_evento(self):
        """
        Verifica que se puede crear y guardar una instancia del modelo Evento.
        """
        # Crear una instancia del modelo Evento
        evento = Evento.objects.create(
            nombre="Concierto de Rock",
            fecha="2025-12-31", # Las fechas y horas en strings pueden ser problemáticas, pero para el test inicial sirve.
            hora="20:00:00",
            ubicacion="Estadio Nacional",
            tipo="presencial", # Asegúrate de que el tipo sea uno de los valores permitidos si tienes choices
            descripcion="Un gran concierto de fin de año."
        )

        # Verificar que la instancia fue creada correctamente y tiene los datos esperados
        self.assertEqual(evento.nombre, "Concierto de Rock")
        self.assertEqual(evento.ubicacion, "Estadio Nacional")
        self.assertEqual(evento.tipo, "presencial")
        self.assertEqual(evento.descripcion, "Un gran concierto de fin de año.")
        # Para campos de fecha y hora, es mejor comparar objetos date/time si los conviertes
        # self.assertEqual(str(evento.fecha), "2025-12-31") # Convertir a string para comparación simple

        # Verificar que el objeto existe en la base de datos
        self.assertTrue(Evento.objects.filter(nombre="Concierto de Rock").exists())

    def test_evento_str_method(self):
        """
        Verifica que el método __str__ del modelo Evento devuelve el nombre correcto.
        """
        evento = Evento.objects.create(
            nombre="Conferencia Tech",
            fecha="2026-01-15",
            hora="09:00:00",
            ubicacion="Centro de Convenciones",
            tipo="virtual",
            descripcion="Charla sobre IA."
        )
        self.assertEqual(str(evento), "Conferencia Tech")

# Puedes añadir más clases de test para otras partes de tu aplicación:
# class MyViewTest(TestCase):
#     def test_home_page_loads(self):
#         response = self.client.get(reverse('home_page_name_in_urls')) # Si tienes una URL con nombre
#         self.assertEqual(response.status_code, 200)