from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from core_apps.commons.models import TimeStampedModel


class Corretora(TimeStampedModel):
    nome_corretora = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Nome Corretora"))
    telefone = PhoneNumberField(max_length=30, blank=False, null=False, verbose_name=_("Telefone"), default='+5544991234567')
    email = models.EmailField(verbose_name=_("Email"), unique=True, db_index=True, null=False, blank=False)
    cnpj = models.CharField(max_length=18, blank=True, null=True, verbose_name=_("CNPJ"), unique=True)
    pessoa_contato = models.CharField(max_length=100, blank=False, null=False, verbose_name=_('Contato'))
    concordo = models.BooleanField(blank=False, null=False, verbose_name=_('Concordo'))

    def __str__(self):
        return self.nome_corretora

    class Meta:
        verbose_name = _("Corretora")
        verbose_name_plural = _("Corretoras")
