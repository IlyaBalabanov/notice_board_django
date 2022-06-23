from django import forms
from django.forms.models import ModelForm
from user_auth.models import Account, Address
# from utils.widgets import CustomTextInput, CustomEmailInput, CustomPasswordInput
from django.forms.widgets import TextInput, Textarea


# TODO: move to file

class CustomTextInput(TextInput):
    input_type = 'text'
    template_name = 'widgets/text_input.html'


class CustomEmailInput(TextInput):
    input_type = "email"
    template_name = 'widgets/text_input.html'


class CustomPasswordInput(TextInput):
    input_type = "password"
    template_name = 'widgets/text_input.html'


class CustomTextArea(Textarea):
    input_type = "password"
    template_name = 'widgets/textarea.html'


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'first_name', 'last_name', 'image')

    username = forms.CharField(max_length=255, label='Логин', widget=CustomTextInput)
    email = forms.EmailField(max_length=255, label='Почта', widget=CustomEmailInput)
    password = forms.CharField(label='Пароль', widget=CustomPasswordInput)

    first_name = forms.CharField(max_length=255, label='Имя', widget=CustomTextInput)
    last_name = forms.CharField(max_length=255, label='Фамилия', widget=CustomTextInput)

    image = forms.FileField(label='Аватар', required=False)


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

    # TODO: max_length
    city = forms.CharField(max_length=255, label='Город', widget=CustomTextInput)
    population_centers = forms.CharField(max_length=255, label='Населенный пункт', widget=CustomTextInput)
    street = forms.CharField(max_length=255, label='Улица', widget=CustomTextInput)
    house = forms.CharField(max_length=255, label='Дом', widget=CustomTextInput)
    building = forms.CharField(max_length=255, label='Корпус', widget=CustomTextInput)
    flat = forms.CharField(max_length=255, label='Квартира', widget=CustomTextInput)
