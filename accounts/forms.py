from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Ensure you're importing your custom User model
from .models import Profile 

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    church = forms.CharField(max_length=100)
    favorite_verse = forms.CharField(max_length=200)
    ministry_interests = forms.CharField(widget=forms.Textarea)
    bio = forms.CharField(widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'password1', 'password2', 'church', 'favorite_verse',
            'ministry_interests', 'bio', 'profile_picture'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ministry_interests': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'favorite_verse': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'church': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'



