from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, CategoryViewSet, TaskViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('categories', CategoryViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
]