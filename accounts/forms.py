from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe 
from haipumpfinder.models import Patient
from django.contrib.admin.widgets import AdminDateWidget

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')
    
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

class PatientForm(forms.ModelForm):
   
    dx_date = forms.DateField(widget=AdminDateWidget)
    dx_date.label = mark_safe('<strong>DX Date</strong>')
    last_treatment_date = forms.DateField(widget=AdminDateWidget)
    last_treatment_date.label = mark_safe('<strong>Last Treatment</strong>')

    class Meta:
        model = Patient
        fields = ('dx_date', 'last_treatment_date', 'ned', 'stage_now', 'stage_at_dx', 'msi_status', 'biomarkers')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')