from django.urls import path
from .views import page

urlpatterns = [
    path('pagina/<str:slug>/', page, name="page"),
]