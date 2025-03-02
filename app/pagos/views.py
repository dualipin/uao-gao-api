from rest_framework.viewsets import ModelViewSet
from .serializers import PagoSerializer, ConceptoSerializer
from .models import Pago, Concepto


class PagoViewSet(ModelViewSet):
    serializer_class = PagoSerializer
    queryset = Pago.objects.all()


class ConceptoViewSet(ModelViewSet):
    serializer_class = ConceptoSerializer
    queryset = Concepto.objects.all()
