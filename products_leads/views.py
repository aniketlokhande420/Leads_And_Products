from django.shortcuts import render

# Create your views here.
from rest_framework import views, viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count
from django.db.models.functions import TruncDate
from .models import Product, Lead
from .serializers import ProductSerializer, LeadSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LeadCreateAPIView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = []  # No authentication required


class LeadsBetweenDatesAPIView(generics.ListAPIView):
    serializer_class = LeadSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        print(start_date, end_date)
        return Lead.objects.filter(created_at__range=[start_date, end_date])

# Top 10 Products with Most Leads
class ProductsWithMostLeadsAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.annotate(num_leads=Count('leads')).order_by('-num_leads')[:10]

# Bottom 10 Products with Least Leads
class ProductsWithLeastLeadsAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.annotate(num_leads=Count('leads')).order_by('num_leads')[:10]

# Number of Products Inquired by Each Lead
class ProductsInquiredPerLeadAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        # Annotate each lead with the count of products they have inquired about
        leads = Lead.objects.annotate(num_products=Count('interested_products'))
        data = [{'lead': lead.name, 'products_count': lead.num_products} for lead in leads]
        return Response(data)
    