from django.urls import path
from pms.views import (
    inputip,
)

from gitpull.views import (
    dashboard,
    output,
    pullutility,
    ssh_dashboard,
    delete,
   
)

urlpatterns= [
    path('', view=ssh_dashboard, name='ssh_dashboard'),
    path('dashboard/', view=dashboard, name='dashboard'),
    path('output/', view=output, name='output'),
    path('pullutility/', view=pullutility, name='pullutility'),
    path('inputip/', view=inputip, name='inputip'),
    path('delete/', view=delete, name='delete'),

]
