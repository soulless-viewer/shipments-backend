from django.urls import include, path
from shipment import views


urlpatterns = [
    path('api/v1/', include('shipment.urls'))
]
