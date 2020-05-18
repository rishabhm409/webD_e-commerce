from django.conf.urls import url,include
from . import views
urlpatterns=[
    url(r'^$',views.index,name='ShopHome'),
    url(r'^about/',views.about,name='AboutUs'),
    url(r'^contact',views.contact,name='ContactUs'),
    url(r'^tracker',views.tracker,name='TrackerStatus'),
    url(r'^search',views.search,name='Search'),
    url(r'^productview/(?P<id>\d+)$',views.productview,name='productview'),
    url(r'^checkout',views.checkout,name='Checkout'),
    #url(r'^$',views.index,name='ShopHome'),
    #url(r'^$',views.index,name='ShopHome'),
    #url(r'^$',views.index,name='ShopHome'),





]