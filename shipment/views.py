from rest_framework import viewsets
from shipment.models import Shipment
from rest_framework.response import Response
from collections import OrderedDict

from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination

from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from shipment.serializers import ShipmentSerializer
from rest_framework.settings import api_settings


# Both "ViewSet" and "view function" approaches are used as demo
class ShipmentListViewSet(viewsets.ViewSet):
    def list(self, request):
        shipments = Shipment.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size_query_param = "page_size"
        shipments_paginated = paginator.paginate_queryset(shipments, request)
        serializer = ShipmentSerializer(shipments_paginated, many=True)
        return Response(
            OrderedDict(
                [
                    (
                        "page",
                        int(request.query_params.get(
                            paginator.page_query_param,
                            1
                        )),
                    ),
                    ("count", paginator.page.paginator.count),
                    ("next", paginator.get_next_link()),
                    ("previous", paginator.get_previous_link()),
                    ("page_size", paginator.page_size),
                    ("results", serializer.data),
                ]
            )
        )

    def create(self, request):
        data = JSONParser().parse(request)
        serializer = ShipmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


def shipment(request, pk):
    try:
        shipment = Shipment.objects.get(pk=pk)
    except Shipment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ShipmentSerializer(shipment)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ShipmentSerializer(shipment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        shipment.delete()
        return HttpResponse(status=204)

    else:
        return HttpResponse(status=405)
