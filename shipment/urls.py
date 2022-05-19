from django.urls import path
from shipment import views


# Both "ViewSet" and "view function" approaches are used as demo
urlpatterns = [
    path(
        "shipment/",
        views.ShipmentListViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path("shipment/<int:pk>/", views.shipment),
]
