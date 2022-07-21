from django.conf.urls import url
from django.contrib import admin
from m3 import get_app_urlpatterns

from app.views import workspace

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', workspace),
]

# Собираем шаблоны урлов из app_meta
# подключенных приложений
urlpatterns.extend(get_app_urlpatterns())
