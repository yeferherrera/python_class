from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludo),
    path('dameFecha/',views.dameFecha),
    path('panel_kenner/', views.panel_kenner),
]