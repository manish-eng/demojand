from django.urls import path
from softwaresversions.views import (
    softwares_versions,
    softwares_versions_view,
    
)

urlpatterns= [
    
    path('softwares_versions/',view=softwares_versions, name='softwares_versions'),
    path('softwares_versions_view/',view=softwares_versions_view, name='softwares_versions_view'),

]
