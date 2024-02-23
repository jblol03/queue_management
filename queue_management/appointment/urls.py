from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DayViewSet, AppointmentViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'days', DayViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls), name='appointment'),
]
