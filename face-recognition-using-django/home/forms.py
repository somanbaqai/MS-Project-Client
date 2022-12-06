from django import forms
from home.models import UserProfile, ModelConfiguration

class RegisterForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'face_id',
            'name',
            'address',
            'job',
            'phone',
            'email',
            'bio',
            'image',
        )

class ModelConfigurationForm(forms.ModelForm):

    class Meta:
        model = ModelConfiguration
        fields = (
            'endpointForFetching',
            'endpointForPosting',
        )