from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path(r'', include('app.urls')),

    path(r'api/v1/', get_schema_view(
        title='Traffic camera monitoring system',
        description='Traffic camera monitoring system: adding, deleting, and editing cameras, detecting errors and '
                    'failures, and ordering maintenance.',
        version='0.1.0'
    ), name='openapi-schema'),

    path(r'api/token/', TokenObtainPairView.as_view()),
    path(r'api/token/refresh/', TokenRefreshView.as_view()),
    path(r'api/token/verify/', TokenVerifyView.as_view()),

    path(r'admin/', admin.site.urls),
]
