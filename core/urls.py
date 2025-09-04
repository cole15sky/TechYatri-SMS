from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, TeacherViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('api/', include(router.urls)),
]
