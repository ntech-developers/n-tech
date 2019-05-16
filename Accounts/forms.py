from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile
class SignUpForm(UserCreationForm):
    SKIll_LEVEL = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    )

    COUNTRY = (
        ('Kenya', 'Kenya'),
        ('Rwanda', 'Rwanda'),
      ('Uganda', 'Uganda'),
        
    )


    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    )

    language = forms.CharField(max_length=100)
    skill_level = forms.ChoiceField(choices=SKIll_LEVEL,
                                    label="",
                                    initial='',
                                    widget=forms.Select(),
                                    required=True)

    institution = forms.CharField(max_length=50)

    gender =  forms.ChoiceField(choices=GENDER,
                                    label="",
                                    initial='',
                                    widget=forms.Select(),
                                    required=True)
                                    
    country =  forms.ChoiceField(choices=COUNTRY,
                                    label="",
                                    initial='',
                                    widget=forms.Select(),
                                    required=True)

    phone_number = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'institution','phone_number','gender','country', 'language',
                  'skill_level')
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)


        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('login', 'Login', css_class='blue-btn')
            )
        )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email',]


class ProfileUpdateForm(forms.ModelForm):

    SKIll_LEVEL = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    )

    COUNTRY = (
        ('Kenya', 'Kenya'),
        ('Rwanda', 'Rwanda'),
      ('Uganda', 'Uganda'),
        
    )


    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    )
    skill_level = forms.ChoiceField(choices=SKIll_LEVEL,
                                    label="",
                                    initial='',
                                    widget=forms.Select(),
                                    required=True)

    gender =  forms.ChoiceField(choices=GENDER,
                                    label="",
                                    initial='',
                                    widget=forms.Select(),
                                    required=True)
                                    
    country =  forms.ChoiceField(choices=COUNTRY,
                                    label="",
                                    initial='',
                                    widget=forms.Select(),
                                    required=True)

    class Meta:
        model = Profile
        fields = ['institution','skill_level','language','gender','country']