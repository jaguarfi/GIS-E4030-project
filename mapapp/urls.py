from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ui, name="mapview"),
    path('TIK_data/<int:floor>/', views.TIK, name="TIK"),
    path('TUAS_data/<int:floor>/', views.TUAS, name="TUAS"),
]