from django.urls import path
from servicestatus.views import (
    # service_status_view,
    service_status,
    service_status_auth_view
)

urlpatterns= [
    
    # path('service_status_view/',view=service_status_view, name='service_status_view'),
    path('service_status/',view=service_status, name='service_status'),
    path('service_status_auth_view/',view=service_status_auth_view, name='service_status_auth_view'),


]
