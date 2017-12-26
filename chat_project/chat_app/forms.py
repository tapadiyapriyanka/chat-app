from django import forms
from .models import chatmessage

class Post_Form(forms.ModelForm):
    class Meta:
        model = chatmessage
        fields = [
            "textmsg",
        ]
