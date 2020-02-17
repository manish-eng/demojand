from django import forms

class PostForm(forms.Form):
  your_IP = forms.CharField(widget=forms.TextInput(attrs={

                'style': 'border-color: skyblue;',
                'placeholder': 'Write your IP here'
            }
  )
  )