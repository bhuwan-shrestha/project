from django.urls import path
from webpage import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('collection', views.collection, name="collection"),
    path('contact', views.contactPage, name="contact"),
    path('inner_feature', views.innerFeature, name='feature'),
]