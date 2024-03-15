from django.urls import path
from details.views import CategoryView, Sub_CategoryView, OrganizationView

urlpatterns=[
path('category/', CategoryView.as_view(), name='category'),
path('subcategory/', Sub_CategoryView.as_view(), name='sub category'),
path('organization/', OrganizationView.as_view(), name='sub category'),

]