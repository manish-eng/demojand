from django import forms


SERVICE_NAMES= [
    ('dvs', 'dvs'),
    ('oneauth','oneauth'),
    ('push-manager', 'push-manager'),
    ('system-monitor','system-monitor'),
    ('cms','cms'),
    ('dashboard','dashboard'),
    ('digivalet-api','digivalet-api'),
    ('digivalet-cloud-api','digivalet-cloud-api'),
    ('digivalet-pmsi','digivalet-pmsi'),
    ('digivalet-posi','digivalet-posi'),
    ('dv-services-api','dv-services-api'),
    ('dv-services-cloud-api','dv-services-cloud-api'),
    ('gateway-services','gateway-services'),
    ('printer-mailer','printer-mailer'),
    ('service-assistance','service-assistance'),
    ('digivalet-butler','digivalet-butler'),
    ('butler-system','butler-system~'),
    ('digivalet-zigbee','digivalet-zigbee'),
    ('digivalet-entertainment','digivalet-entertainment'),
    ('digivalet-cloud-db','digivalet-cloud-db'),
    ('digivalet-db','digivalet-db'),
    ('digivalet-dvs-db','digivalet-dvs-db'),
    ('digivalet-mymovie-db','digivalet-mymovie-db'),
    ('digivalet-oneauth-db','digivalet-oneauth-db'),
    ('digivalet-butler-db','digivalet-butler-db'),
]


class VersionForm(forms.Form):
    select_software = forms.CharField(label='Select Software', widget=forms.Select(choices=SERVICE_NAMES,attrs={
        'style': 'border-color: skyblue; width:  100%; border-style: solid;   border-width: 5px;; '
    }))

