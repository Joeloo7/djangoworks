from django.forms import ChoiceField
from django.contrib.auth.forms import UserCreationForm
from authentication.users import forms
from users.models import CustomUser


class SignupForm(UserCreationForm):
    role_choices=(('student,Student'),('teacher','Teacher'))
    role=forms.ChoiceField(choices=role_choices)

    gender_choices = (('male,Male'), ('female','Female'))
    gender = forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    class Meta:
        model=CustomUser
        fields=['username','password1','password2','email','first_name','last-name','phone','role','gender']