from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:week_day>', views.week_days_by_number),
    path('<str:week_day>', views.week_days_by_day, name='week_day_name')
]