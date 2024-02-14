from django.urls import path
from .views import DayListCreateView, ShiftListCreateView, SlotListCreateView, ScheduleViewSet

urlpatterns = [
    path('', ScheduleViewSet.as_view({'get': 'list', 'post': 'create'}), name='schedule'),
    path('day/<int:pk>/', DayListCreateView.as_view(), name='day_detail'),
    path('shift/', ShiftListCreateView.as_view(), name='shift'),
    path('shift/<int:pk>/', ShiftListCreateView.as_view(), name='shift_detail'),
    path('slot/', SlotListCreateView.as_view(), name='slot'),
    path('slot/<int:pk>/', SlotListCreateView.as_view(), name='slot_detail'),
]
