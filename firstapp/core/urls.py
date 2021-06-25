from django.urls import path
from . import views

urlpatterns = [
    path('<int:n1>/<int:n2>/', views.soma, name='soma'),
    path('hello/', views.hello, name='hello'),
    path('seila/', views.seila, name='seila'),
]