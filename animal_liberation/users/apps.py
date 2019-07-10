from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "animal_liberation.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import animal_liberation.users.signals  # noqa F401
        except ImportError:
            pass
