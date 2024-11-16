from django.apps import AppConfig


class NaijaKitchenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'naija_kitchen'

    def ready(self):
        import naija_kitchen.signals
