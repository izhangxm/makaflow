from django.apps import AppConfig
from apps.makaflow.tasks import start_tasks
from apps.makaflow.tasks import load_all
class MakaflowConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.makaflow"
    verbose_name = "Makaflow"
    def ready(self) -> None:
        super().ready()
        from apps.makaflow import urls
        try:
            urls.init()
            load_all()
            start_tasks()
            
        except Exception as e:
            print(e)