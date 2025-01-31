from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from django.shortcuts import redirect

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('',lambda request:redirect(router.urls)),
]
