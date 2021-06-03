from rest_framework.routers import DefaultRouter
from .viewsets import NoteViewSet


# Создаем router и регистрируем ViewSet
router = DefaultRouter()
router.register('notes', NoteViewSet)
# URLs настраиваются автоматически роутером

app_name = 'notes'

urlpatterns = router.urls
