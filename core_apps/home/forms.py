from django import forms
from utils.django_forms import add_placeholder
from .models import Corretora


class CorretoraForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['nome_corretora'], 'Nome da corretora.')
        add_placeholder(self.fields['telefone'], 'Seu telefone.')
        add_placeholder(self.fields['email'], 'Seu email.')
        add_placeholder(self.fields['cnpj'], 'Seu cnpj.')
        add_placeholder(self.fields['pessoa_contato'], 'Contato')

    nome_corretora = forms.CharField(
        label='Nome da Corretora',
        help_text='Somente caracteres válidos.',
        error_messages={
            'required': 'Este campo não pode ficar em branco!',
        },
    )
    telefone = forms.CharField(
        label='Telefone ou Celular',
        help_text='Digite um telefone ou celular válido.',
        error_messages={
            'required': 'Este campo não pode ficar em branco!',
        },
    )
    email = forms.EmailField(
        label='E-mail',
        help_text='Digite um e-mail válido.',
        error_messages={
            'required': 'Este campo não pode ficar em branco!'
        },
    )
    cnpj = forms.CharField(
        label='CNPJ',
        help_text='Digite um CNPJ válido.',
    )
    pessoa_contato = forms.CharField(
        label='Contato',
        help_text='Digite seu nome.'
    )

    class Meta:
        model = Corretora
        fields = ['nome_corretora', 'telefone', 'email', 'cnpj', 'pessoa_contato', 'concordo']

    error_messages = {
        "duplicate_email": "Um formulário com este e-mail já foi enviado.",
        "duplicate_cnpj": "Um formulário com este CNPJ já foi enviado.",
        "cnpj_error": "O CNPJ deve conter apenas números.",
        "telefone_error": "O telefone deve conter apenas números.",
    }

    def clean_email(self) -> str:
        email = self.cleaned_data["email"]
        if Corretora.objects.filter(email=email).exists():
            raise forms.ValidationError(self.error_messages["duplicate_email"])
        return email

    def clean_cnpj(self) -> str:
        cnpj = self.cleaned_data["cnpj"]
        if not cnpj.isdigit():
            raise forms.ValidationError(self.error_messages["cnpj_error"])
        if Corretora.objects.filter(cnpj=cnpj).exists():
            raise forms.ValidationError(self.error_messages["duplicate_cnpj"])
        return cnpj

    def clean_telefone(self) -> str:
        telefone = self.cleaned_data["telefone"]
        if not telefone.isdigit():
            raise forms.ValidationError(self.error_messages["telefone_error"])
        return telefone
