from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('create/', views.create_person_view, name='create-person'),
    path('read/', views.read_persons_view, name='read-persons'),
    path('update/', views.update_person_view, name='update-person'),
    path('delete/', views.delete_person_view, name='delete-person'),

    path('obtener-lista-personas/', views.obtener_lista_personas, name='obtener-lista-personas'),
    path('crear-persona/', views.crear_persona, name='crear-persona'),
    path('obtener-detalles-persona/', views.obtener_detalles_persona, name='obtener-detalles-persona'),
    path('actualizar-persona/', views.actualizar_persona, name='actualizar-persona'),
    path('eliminar-persona/', views.eliminar_persona, name='eliminar-persona'),
]
