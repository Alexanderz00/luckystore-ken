from django.urls import path
from . import views


#urlpatterns = [
#  path('contact', views.contact, name='contact')
#]


urlpatterns = [
  path('contact', views.contact, name='contact')
]
