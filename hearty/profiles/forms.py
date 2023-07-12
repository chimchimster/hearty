from django import forms
from .models import Images, Profile


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'id': 'file-input', 'style': 'opacity: 0;'})
        }
        labels = {
            'image': '',
        }
