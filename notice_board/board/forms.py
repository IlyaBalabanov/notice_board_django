from django import forms
from django.forms.models import ModelForm

from board.models import Notice
from user_auth.forms import CustomTextInput, CustomTextArea


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('title', 'text', 'image')

    title = forms.CharField(max_length=255, label='Заголовок', widget=CustomTextInput)
    text = forms.CharField(max_length=2550, label='Текст', widget=CustomTextArea)
    image = forms.FileField(label='Картинка', required=False)
