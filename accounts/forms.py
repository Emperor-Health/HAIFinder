from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')
    #first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    
    #last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Screen '}))
    username.label = mark_safe('<strong>User Name</strong>')

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    email.label = mark_safe('<strong>Email</strong>')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password1.label = mark_safe('<strong>Password</strong>')
 
    #password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confim Password'}))
    #password2.label = mark_safe('<strong>Confirm   Password</strong>')
    class Meta:
        model = User
        #fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = ('username', 'email', 'password1' )