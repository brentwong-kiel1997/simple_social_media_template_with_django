from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile, Message

class Custom_user_creation_form(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'email', 'username', 'password1', 'password2']
        labels = {'username': 'User Name', 'email': 'Email'}

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('This username is already taken.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already registered.')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class Profile_form(ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name',
                  'email',
                  'location',
                  'bio',
                  'profile_image']


class Message_form(ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        readonly_fields = ['body']