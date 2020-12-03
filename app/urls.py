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
]

urlpatterns += router.urls
