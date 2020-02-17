from django.urls import path
from pms.views import (
    inputip,
)

from gitpull.views import (
    dashboard,
    # output,
    # pullutility,
    delete,
    ssh_dashboard,
    index_view,
   
)

urlpatterns= [
    path('', view=index_view, name='index_view'),
    path('ssh_dashboard', view=ssh_dashboard, name='ssh_dashboard'),
    path('dashboard/', view=dashboard, name='dashboard'),
    path('delete/', view=delete, name='delete'),
    # path('output/', view=output, name='output'),
    # path('pullutility/', view=pullutility, name='pullutility'),
    path('inputip/', view=inputip, name='inputip'),

]
