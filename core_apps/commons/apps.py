from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommonsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.commons"
    verbose_name = _("Commons")
