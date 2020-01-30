from django import forms


SERVICE_NAMES= [
    ('printer-mailer', 'printer-mailer'),
    ('digivalet-pmsi','digivalet-pmsi'),
    ('nodejs-core', 'nodejs-core'),
    ('nodejs-cloud-core','nodejs-cloud-core'),
    ('nodejs-dashboard','nodejs-dashboard'),
    
    ('digivalet-entertainment','digivalet-entertainment'),
    ('push-manager','push-manager'),
    ('system-monitor','system-monitor'),
    ('digivalet-posi','digivalet-posi'),
    ('gateway-services',' gateway-services'),
    ('service-assistance','service-assistance'),
    ('nodejs-butler','nodejs-butler'),
    ('digivalet-butler','digivalet-butler'),
    ('digivalet-zigbee','digivalet-zigbee'),
    ('content-service','content-service'),
    ('content-service-celery-worker','content-service-celery-worker'),
    ('content-service-celery-beat','content-service-celery-beat'),






]

class AuthForm(forms.Form):
    # username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
    #     'style': 'border-color: skyblue; width:  100%;  ; '
    # }))
    # password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
    #     'style': 'border-color: skyblue; width:  100%;  ; '
    # }))
    # server_IP = forms.CharField(label='Server IP', widget=forms.TextInput(attrs={
    #     'style': 'border-color: skyblue; width:  100%;  ; '
    # }))
    select_service = forms.CharField(label='Select Service', widget=forms.Select(choices=SERVICE_NAMES,attrs={
        'style': 'border-color: skyblue; width:  100%; border-style: solid;   border-width: 5px;; '
    }))

# class SelectForm(forms.Form):
#     select_service = forms.CharField(label='Select Service', widget=forms.Select(choices=SERVICE_NAMES,attrs={
#         'style': 'border-color: grey; width:  100%; border-style: solid;  ; '
#     }))

