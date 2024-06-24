from django.urls import path
from .views import CadastroCorretoraView


urlpatterns = [
    path('', CadastroCorretoraView.as_view(), name='cadastro_corretora'),
]
