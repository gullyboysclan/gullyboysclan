from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.

class StoreView(View):
    products = Product.objects.all().order_by('product_ordering')

    def get(self,request):
        context ={
            'products':self.products,
        }
        return render(request,'store.html',context)

class ProductDetailView(View):

    def get(self,request,unique_id):
        product = Product.objects.get(unique_id=unique_id)
        context ={
            'product':product,
        }
        return render(request,'productDetail.html',context)

class HomePageView(View):

    def get(self,request):
        return render(request,'home.html')

def checkout(request):
    # if request.method == 'POST':
    #     if 'pay' in request.POST:
    #         cartData = request.POST.get('cartData')
    #         cartData =ast.literal_eval(cartData)

            

    #         # delivery info 
    #         firstName = request.POST.get('fname')
    #         lastName = request.POST.get('lname')
    #         email = request.POST.get('email')
    #         phone = request.POST.get('phone')
    #         orderNotes = request.POST.get('orderNotes')
    #         street_address_1 = request.POST.get('street_address_1')
    #         street_address_2 = request.POST.get('street_address_2')
    #         city = request.POST.get('city')
    #         state = request.POST.get('state')
    #         zip_code = request.POST.get('zip')
    #         destination_country = request.POST.get('destination_country')
    #         deliveryInfo = request.POST.get('deliveryInfo')
    #         cart_total = request.POST.get('cart-total')
    #         country_code = request.POST.get('country_code')

    #         payment = Payment(first_name=firstName,last_name=lastName,email=email,country_code=country_code,phone=phone,order_notes=orderNotes,street_address_1=street_address_1,street_address_2=street_address_2,city=city,state=state,zip_code=zip_code,destination_country=destination_country,additional_info=deliveryInfo,amount=float(cart_total))
    #         payment.save()
            
    #         # on payment save create cart for payment
    #         cart = Cart.objects.get_or_create(payment=payment) # create cart for payment
    #         cart[0].save()

    #         # loop through cart object list to append to cart
    #         for obj in cartData:
    #             product = Product.objects.get(unique_id=obj['product_id'])
    #             cartObj = CartObject(cart=cart[0],product=product,size=obj['selectedSize'],quantity=obj['quantity'] )
    #             cartObj.save()


    #         return redirect(makePayment,payment.ref)

     
    return render(request,'checkout.html')
