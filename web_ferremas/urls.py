from django.urls import path, include
from .views import *

urlpatterns = [
    path('base/', base, name='BASE'),
    path('', index, name='INDEX'),
    path('login/', login, name='LOGIN'),
    path('cerrar_sesion/', cerrar_sesion, name='CERRAR_SESION'),
    path('registro/', registro, name='REGISTRO'),
    path('productos/', productos, name='PRODUCTOS'),
    path('perfil/', perfil_usuario, name='PERFIL_USUARIO'),
    path('perfil/actualizar/', actualizar_perfil, name='actualizar_perfil'),
    # path('crud_productos/', crud_productos, name='CRUD_PRODUCTOS'),
    #
    path('categoriaprod/<int:categoriaprod_id>/', categoriaprod, name="categoriaprod"),
    path('tipoprod/<int:tipoprod_id>/', tipoprod, name="tipoprod"),

    # CARRITO
    path('carrito/', carrito, name='CARRITO'),

    # METODOS PRINCIPALES
    path('agregar/<int:id_producto>/', agregar_al_carrito, name='AGREGAR_AL_CARRITO'),
    path('eliminar/<int:id_item>/', eliminar_del_carrito, name='ELIMINAR_DEL_CARRITO'),
    path('vaciar/', vaciar_carrito, name='VACIAR_CARRITO'),

    # AUMENTAR Y DISMINUR CANTIDAD
    path('aumentar/<int:id_item>/', aumentar_cantidad, name='AUMENTAR_CANTIDAD'),
    path('disminuir/<int:id_item>/', disminuir_cantidad, name='DISMINUIR_CANTIDAD'),

    # MERCADO PAGO
    # path('checkout/', checkout, name='checkout'),
    # path('success/', success, name='success'),
    # path('failure/', failure, name='failure'),
    # path('pending/', pending, name='pending'),

    # WEBPAY PLUS
    path('webpay-plus/create', webpay_plus_create, name='webpay_plus_create'),
    path('webpay-plus/commit', webpay_plus_commit, name='webpay_plus_commit'),
    path('webpay-plus/commit-error', webpay_plus_commit_error, name='webpay_plus_commit_error'),
    path('webpay-plus/refund', webpay_plus_refund, name='webpay_plus_refund'),
    path('webpay-plus/refund-form', webpay_plus_refund_form, name='webpay_plus_refund_form'),
    path('webpay-plus/status-form', show_create, name='webpay_plus_status_form'),
    path('webpay-plus/status', status, name='webpay_plus_status'),
    path('generar-boleta_webpay/', generarBoleta, name='generar_boleta_webpay'),


    # Trabajadores
    # path('vendedor/', vendedor, name='vendedor'),
    # path('categoria/<int:categoria_id>/', categoria, name="categoria"),
    # path('tipo/<int:tipo_id>/', tipo, name="tipo"),
    # path('bodeguero/', bodeguero, name="bodeguero"),
    # path('contador/', contador, name="contador"),

    # Vistas vendedor

    path('ver_productos/', ver_productos, name='ver_productos'),
    path('enviar_orden/<int:pedido_id>/', enviar_orden, name='enviar_orden'),


    path('realizar_pedido/', realizar_pedido, name='REALIZAR_PEDIDO'),
    path('aprobar_pedido/<int:pedido_id>/', aprobar_pedido, name='APROBAR_PEDIDO'),
    path('rechazar_pedido/<int:pedido_id>/', rechazar_pedido, name='RECHAZAR_PEDIDO'),
    path('gestionar_pedidos/', gestionar_pedidos, name='GESTIONAR_PEDIDOS'),
    path('generar_boleta/', generar_boleta, name='GENERAR_BOLETA'),
    path('anular_pedido/<int:pedido_id>/', anular_pedido, name='ANULAR_PEDIDO'),
]