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