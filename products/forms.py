from django import forms
from .models import Comment
from django import forms
from .models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class UserForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=['%d.%m.%Y'],
        help_text='ДД.ММ.ГГГГ'
    )

    class Meta:
        model = User
        fields = '__all__'

