from django import forms
from .models import PrayerRequest, PrayerResponse

class PrayerRequestForm(forms.ModelForm):
    class Meta:
        model = PrayerRequest
        fields = ['title', 'message']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prayer Title'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your prayer request here...'}),
        }

class PrayerResponseForm(forms.ModelForm):
    class Meta:
        model = PrayerResponse
        fields = ['message', 'is_private']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your prayer response here...',
                'rows': 4
            }),
            'is_private': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

