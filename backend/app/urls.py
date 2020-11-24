from django.contrib.auth.decorators import permission_required
from django.urls import path
from rest_framework.routers import SimpleRouter

from app import views
from app.views import *

router = SimpleRouter()

router.register(r'api/v1/city', CityViewSet)
router.register(r'api/v1/location', LocationViewSet)
router.register(r'api/v1/state', StateViewSet)
router.register(r'api/v1/specifications', SpecificationsViewSet)
router.register(r'api/v1/camera', CameraViewSet)
router.register(r'api/v1/service', ServiceViewSet)

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

    # path('service-organizations',
    #      permission_required('app.add_serviceorganization')(views.ServiceOrganizationCreateView.as_view()),
    #      name='service_org_list'),
    # path('service-organizations/update/<int:pk>',
    #      permission_required('app.add_serviceorganization')(views.ServiceOrganizationUpdateView.as_view()),
    #      name='service_org_update'),
    # path('service-organizations/delete/<int:pk>',
    #      permission_required('app.add_serviceorganization')(views.ServiceOrganizationDeleteView.as_view()),
    #      name='service_org_delete'),
]

urlpatterns += router.urls
