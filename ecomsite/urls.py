from django.urls import path
from . import views
app_name='ecomsite'

urlpatterns = [

    path('', views.allproductCat, name='allproductCat'),
    path('<slug:c_slug>/', views.allproductCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.productdetails, name='prodCatDetail'),

]
