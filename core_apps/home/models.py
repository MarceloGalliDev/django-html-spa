from django.db import models
from django.utils.translation import gettext_lazy as _
from core_apps.commons.models import TimeStampedModel


class Corretora(TimeStampedModel):
    nome_corretora = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Nome Corretora"))
    telefone = models.CharField(max_length=15, blank=False, null=False, verbose_name=_("Telefone"))
    email = models.EmailField(verbose_name=_("Email"), unique=True, db_index=True, null=False, blank=False)
    cnpj = models.CharField(max_length=19, blank=True, null=True, verbose_name=_("CNPJ"), unique=True)
    pessoa_contato = models.CharField(max_length=100, blank=False, null=False, verbose_name=_('Contato'))

    def __str__(self):
        return self.nome_corretora

    class Meta:
        verbose_name = _("Corretora")
        verbose_name_plural = _("Corretoras")
