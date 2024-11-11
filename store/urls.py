from django.urls import path
from .views import StoreView, ProductDetailView, HomePageView

urlpatterns = [
    path('store/',StoreView.as_view(),name='store'),
    path('store/product/detail/<str:unique_id>/',ProductDetailView.as_view(),name='productDetail'),
    path('',HomePageView.as_view(),name='homePage')

]