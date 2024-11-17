from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seu Usuário','class': 'w-full py-4 px-6 rounded-xl'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Seu Usuário','class': 'w-full py-4 px-6 rounded-xl'}))


class CadastroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seu Usuário', 'class': 'w-full py-4 px-6 rounded-xl'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Seu E-mail','class': 'w-full py-4 px-6 rounded-xl'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seu Nome','class': 'w-full py-4 px-6 rounded-xl'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Seu Sobrenome','class': 'w-full py-4 px-6 rounded-xl'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Sua Senha','class': 'w-full py-4 px-6 rounded-xl'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Digite Sua Senha Novamente','class': 'w-full py-4 px-6 rounded-xl'}))

    def clean(self):
        cleade =  super().clean()
        password1 = cleade.get("password1")
        password2 = cleade.get("password2")

        print(password1, password2)
        return cleade