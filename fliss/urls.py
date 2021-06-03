from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings


# Регистрируем API
apipatterns = [
    path('', include('apps.notes.api.urls')),
]


urlpatterns = [
    #path('api/v1/', include(apipatterns, 'app_name'), namespace='api'),
    path('api/v1/', include('apps.notes.api.urls')),
    # path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),  # admin site
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = 'notes'
