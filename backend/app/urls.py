from django.contrib.auth.decorators import permission_required
from django.urls import path
from rest_framework.routers import SimpleRouter

from app import views

router = SimpleRouter()

router.register(r'api/v1/city', views.CityViewSet)
router.register(r'api/v1/location', views.LocationViewSet)
router.register(r'api/v1/state', views.StateViewSet)
router.register(r'api/v1/specifications', views.SpecificationsViewSet)
router.register(r'api/v1/camera', views.CameraViewSet)
router.register(r'api/v1/service', views.ServiceViewSet)

urlpatterns = [
    path('legacy/', views.AppLoginView.as_view(), name='login'),
    path('legacy/logout', views.AppLogoutView.as_view(), name='logout'),

    path('legacy/editing', permission_required('app.add_camera')(views.CameraCreateView.as_view()), name='camera_list'),
    path('legacy/editing/delete/<int:pk>', permission_required('app.add_camera')(views.CameraDeleteView.as_view()),
         name='delete_camera'),
    path('legacy/editing/update/<int:pk>', permission_required('app.add_camera')(views.CameraUpdateView.as_view()),
         name='update_camera'),
    path('legacy/audit', permission_required('app.add_camera')(views.ServiceCreateView.as_view()), name='audit_camera'),
    path('legacy/audit/reverse', permission_required('app.add_camera')(views.ServiceCreateReverseView.as_view()),
         name='audit_camera_reverse'),
    path('legacy/audit/services/<int:camera>', permission_required('app.add_camera')(views.ServiceListView.as_view()),
         name='camera_services'),
    path('legacy/audit/services/<int:camera>',
         permission_required('app.add_camera')(views.ServiceListReverseView.as_view()),
         name='camera_services_reverse'),
    path('legacy/audit/detail/<int:pk>', permission_required('app.add_camera')(views.AuditDetailView.as_view()),
         name='audit_detail'),
]

urlpatterns += router.urls
