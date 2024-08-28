from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorsSerializer, MeasurementCreateSerializer, SensorDetailSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

# class SensorsView(ListAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer
#
#     def post(self, request):
#         return Response(request)
#
# class SensorView(RetrieveAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer

class ListCreateSensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class ListUpdateSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateSerializerView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer