from django import forms
from .models import Images, Like, Dislike


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


class LikeProfileForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = []


class DislikeProfileForm(forms.ModelForm):
    class Meta:
        model = Dislike
        fields = []