#coding: utf-8
from django.utils.translation import ugettext, ugettext_lazy as _

from bus.models import BusStation
from bus.settings import BusSettings, controller

try:
    stations = BusStation.objects.get(name = "Stúdentagarðar")
except BusStation.DoesNotExist:
    stations = []

class StigullBusSettings(BusSettings):
    stations = stations
controller.register(StigullBusSettings)




