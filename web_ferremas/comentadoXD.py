
### fin carrito
# MERCADOPAGO_ACCESS_TOKEN = 'TEST-2707703782990962-052210-1c16fe9d61ba257bc74b01bf7721ba4a-1821506213'

# MERCADO PAGO UWU
# @login_required(login_url='/login/')  # Asegura que el usuario esté autenticado
# def checkout(request):
#     usuario = request.user
#     try:
#         carrito = Carrito.objects.get(usuario=usuario)
#     except Carrito.DoesNotExist:
#         # Maneja el caso en que el carrito no existe para el usuario
#         return redirect('CARRITO')

#     items = []
#     for item in CarritoItem.objects.filter(carrito=carrito):
#         items.append({
#             "title": item.producto.nombre,
#             "quantity": item.cantidad,
#             "currency_id": "CLP",  # Ajusta según la moneda que estés utilizando
#             "unit_price": float(item.producto.precio)  # Utiliza el precio del producto
#         })

#     sdk = mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN)

#     try:
#         preference_data = {
#             "items": items,
#             "back_urls": {
#                 "success": 'http://127.0.0.1:8000/success/',
#                 "failure": 'http://127.0.0.1:8000/failure/',
#                 "pending": 'http://127.0.0.1:8000/pending/'
#             },
#             "auto_return": "approved",
#         }
#         preference_response = sdk.preference().create(preference_data)
#         preference = preference_response["response"]

#         return render(request, "payments/checkout.html", {
#             "preference_id": preference["id"]
#         })
#     except Exception as e:
#         # Maneja el error de manera adecuada, puede ser un log, redirección a una página de error, etc.
#         print("Error al crear la preferencia de pago:", e)
#         return redirect('CARRITO')


# def success(request):
#     return render(request, "payments/success.html")

# def failure(request):
#     return render(request, "payments/failure.html")

# def pending(request):
#     return render(request, "payments/pending.html")





# def is_vendedor(user):
#     return user.groups.filter(name='vendedor').exists()

# @user_passes_test(is_vendedor, login_url='/login/')
# def vendedor(request):
#     productos_list = Producto.objects.all()
#     categorias_list = CategoriaProducto.objects.all()
#     paginator = Paginator(productos_list, 10) 
#     tipos_list = TipoProducto.objects.all()


#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     ctx = {
#         "page_obj": page_obj,
#         "categorias": categorias_list,
#         "tipos": tipos_list,

#     }
#     return render(request, "trabajadores/vendedor/vendedor.html", ctx)

# @user_passes_test(is_vendedor, login_url='/login/')
# def categoria(request, categoria_id):
#     categoria = get_object_or_404(CategoriaProducto, id=categoria_id)
#     categorias_list = CategoriaProducto.objects.all()

#     tipos_list = TipoProducto.objects.all()

#     productos = Producto.objects.filter(categoria=categoria)
#     paginator = Paginator(productos, 6) 

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     ctx = {
#         "page_obj": page_obj,
#         "categoria": categoria,
#         "categorias": categorias_list,
#         "tipos": tipos_list,


#     }
#     return render(request, "trabajadores/vendedor/categoria.html", ctx)

# @user_passes_test(is_vendedor, login_url='/login/')
# def tipo(request, tipo_id):
#     tipo = get_object_or_404(TipoProducto, id=tipo_id)
#     tipos_list = TipoProducto.objects.all()

#     categorias_list = CategoriaProducto.objects.all()

#     productos = Producto.objects.filter(tipo=tipo)
#     paginator = Paginator(productos, 6) 

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     ctx = {
#         "page_obj": page_obj,
#         "tipo": tipo,
#         "tipos": tipos_list,
#         "categorias": categorias_list,


#     }
#     return render(request, "trabajadores/vendedor/tipo.html", ctx)


# def is_bodeguero(user):
#     return user.groups.filter(name='bodeguero').exists()


# @user_passes_test(is_bodeguero, login_url='/login/')
# def bodeguero(request):
#     return render(request, 'trabajadores/bodeguero/bodeguero.html')

# def is_contador(user):
#     return user.groups.filter(name='contador').exists()

# @user_passes_test(is_contador, login_url='/login/')
# def contador(request):
#     return render(request, 'trabajadores/contador/contador.html')




# def crud_productos(request):
#     return render(request, 'crud_productos.html')






# def is_vendedor(user):
#     return user.groups.filter(name='vendedor').exists()

# @user_passes_test(is_vendedor, login_url='/login/')
# def vendedor(request):
#     productos_list = Producto.objects.all()
#     categorias_list = CategoriaProducto.objects.all()
#     paginator = Paginator(productos_list, 10) 
#     tipos_list = TipoProducto.objects.all()


#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     ctx = {
#         "page_obj": page_obj,
#         "categorias": categorias_list,
#         "tipos": tipos_list,

#     }
#     return render(request, "trabajadores/vendedor/vendedor.html", ctx)