from django import forms
from .models import chatmessage
from django.forms import TextInput, Textarea

class Post_Form(forms.ModelForm):
    class Meta:
        model = chatmessage
        widgets = {
          'textmsg': forms.Textarea(attrs={'rows':1, 'cols':25})
        }
        fields = [
            "textmsg",
        ]
