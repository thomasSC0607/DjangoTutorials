from django.apps import AppConfig
from django.utils.module_loading import import_string
from django.conf import settings


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

    # Variable de clase para exponer el provider en runtime
    image_storage_class = None

    def ready(self):
        # Carga la clase desde settings
        PagesConfig.image_storage_class = import_string(settings.IMAGE_STORAGE_CLASS)
