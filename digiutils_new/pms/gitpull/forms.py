from django import forms
from .models import GitPull, SSHauth

class GitPullForm(forms.ModelForm):
    class Meta:
        model= GitPull
        widgets = {
        'password': forms.PasswordInput(attrs={

                'style': 'border-color: skyblue;',
            }),
        'username': forms.TextInput(attrs={

                'style': 'border-color: skyblue;',   
            }
  )
    }
        fields= ('__all__')


class SSHForm(forms.ModelForm):
    class Meta:
        model= SSHauth
        widgets = {
        'password': forms.PasswordInput(attrs={

                'style': 'border-color: skyblue;',
            }),
        'username': forms.TextInput(attrs={

                'style': 'border-color: skyblue;',   
            }),
        'server_ip': forms.TextInput(attrs={

                'style': 'border-color: skyblue;',   
            }),
    }
        fields= ('username', 'password', 'server_ip')


# class SSHForm(forms.Form):
#     username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
#         'style': 'border-color: skyblue; width:  100%;  ; '
#     }))
#     password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
#         'style': 'border-color: skyblue; width:  100%;  ; '
#     }))
#     server_IP = forms.CharField(label='Server IP', widget=forms.TextInput(attrs={
#         'style': 'border-color: skyblue; width:  100%;  ; '
#     }))