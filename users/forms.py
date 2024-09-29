from django.forms import ModelForm, CharField, PasswordInput
from django.contrib.auth.models import User

class UserRegistrationForm(ModelForm):
    password = CharField(widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user