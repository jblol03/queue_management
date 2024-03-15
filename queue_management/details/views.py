from rest_framework import generics, status
from rest_framework.response import Response
from details.serializers import OrganizationSerializer, Organization, CategorySerializer, Sub_CategorySerializer, Category, Sub_Category
# from .models import Category, Sub_Category

class CategoryView (generics.GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request):
        category = self.get_queryset()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sub_CategoryView(generics.GenericAPIView):
    serializer_class = Sub_CategorySerializer
    queryset = Sub_Category.objects.all()

    def get(self, request):
        sub_category = self.get_queryset()
        serializer = Sub_CategorySerializer(sub_category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Sub_CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganizationView(generics.GenericAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def get(self, request):
        organization = self.get_queryset()
        serializer = OrganizationSerializer(organization, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
