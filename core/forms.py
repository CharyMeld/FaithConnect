from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Ensure you're importing your custom User model
from post.models import Post


class CustomUserCreationForm(UserCreationForm):
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

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'media_files', 'author']
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Write your post here...',
                'rows': 4
            })
        }
