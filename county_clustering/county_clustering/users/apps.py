from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "county_clustering.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import county_clustering.users.signals  # noqa F401
        except ImportError:
            pass
