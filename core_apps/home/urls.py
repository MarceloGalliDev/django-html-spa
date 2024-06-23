from django.urls import path
from .views import CadastroCorretoraView


urlpatterns = [
    path('cadastro/', CadastroCorretoraView.as_view(), name='cadastro_corretora'),
]
