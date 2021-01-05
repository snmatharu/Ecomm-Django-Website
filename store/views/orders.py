from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.customer import Customer
from django.views import  View
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator

class Orders(View):

    # @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)

        print(orders)

        orders=orders.reverse()
        return render(request, 'order.html', {'orders': orders} )