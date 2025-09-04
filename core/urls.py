from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, TeacherViewSet, StudentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('api-auth/', include('rest_framework.urls')),
]
