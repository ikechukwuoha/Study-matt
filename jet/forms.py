from django.forms import ModelForm
from .models import Room
from django.contrib.auth import get_user_model
from users.forms import CustomUserCreationForm, CustomUserChangeForm


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        
        
        
        
        
class UserForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['name', 'bio', 'avatar', 'username', 'email', 'phone_no', ]
 
        