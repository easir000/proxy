from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_data, name='input_data'),
    path('output/', views.output_data, name='output_data'),
]
