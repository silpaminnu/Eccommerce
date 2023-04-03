from django.contrib import admin
from django.urls import path, include
from. import views
app_name='shop'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetails'),

]
