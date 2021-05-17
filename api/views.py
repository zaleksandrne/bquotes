from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, permissions

from .models import Quote
from .serializers import QuoteSerializer


def index(request):
    return render(request, index, {})

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.AllowAny, ]
