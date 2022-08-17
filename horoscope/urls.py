from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.index2),
    path('<int:sign_zodiac>', views.get_horoscope_by_number),
    path('<str:sign_zodiac>', views.get_horoscope_by_sign, name='horoscope-name'),
    path("type/<str:element>", views.type_element, name='element-name'),

]
