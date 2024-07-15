from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Order





@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order/list.html', {'orders': orders}) 
@login_required
def order_create(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # Opcionalmente, limpia el carrito después de crear el pedido
            cart.clear()
            # Renderiza la página de éxito del pedido
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    
    # Si la solicitud no es POST o el formulario no es válido,
    # renderiza la página de creación de pedido con el formulario y el carrito
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
