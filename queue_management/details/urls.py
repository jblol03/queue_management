from django.urls import path
from details.views import CategoryView, Sub_CategoryView

urlpatterns=[
path('category', CategoryView.as_view(), name='category'),
path('subcategory', Sub_CategoryView.as_view(), name='sub category'),

]