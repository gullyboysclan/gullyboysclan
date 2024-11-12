from django.urls import path
from .views import StoreView, ProductDetailView, HomePageView, checkout, LookBook,ContactForm
urlpatterns = [
    path('store/',StoreView.as_view(),name='store'),
    path('store/product/detail/<str:unique_id>/',ProductDetailView.as_view(),name='productDetail'),
    path('',HomePageView.as_view(),name='homePage'),
    path('checkout/',checkout,name='checkout'),
    path('lookbook/',LookBook.as_view(),name='lookbook'),
    path('contact/',ContactForm.as_view(),name='contact')
]