from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/nuevo/', views.gestionar_producto, name='nuevo_producto'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('producto/<int:id>/editar/', views.gestionar_producto, name='editar_producto'),
    path('producto/<int:id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('importar/', views.importar_productos_api, name='importar_productos'),
]