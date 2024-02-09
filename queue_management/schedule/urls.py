from django.urls import path
from .views import DayListCreateView, ShiftListCreateView, SlotListCreateView

urlpatterns = [
    path('days/', DayListCreateView.as_view(), name='day-list-create'),
    path('shifts/', ShiftListCreateView.as_view(), name='shift-list-create'),
    path('slots/', SlotListCreateView.as_view(), name='slot-list-create'),
]