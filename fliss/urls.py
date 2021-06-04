from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


# Регистрируем API
apipatterns = [
    path('', include('apps.notes.api.urls')),
]


urlpatterns = [
    # path('/', TemplateView.as_view(template_name=''))
    path('api/v1/', include('apps.notes.api.urls')),
    # path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),  # admin site
    path('home/', TemplateView.as_view(template_name='home/home.html'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = 'notes'
