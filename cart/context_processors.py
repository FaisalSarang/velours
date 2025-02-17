from .cart import Cart
 
#Create context processor so that cart can work on all web pages
def cart(request):
    #Return default data from cart
    return {'cart': Cart(request)}