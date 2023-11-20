from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', label_suffix=' - ', initial='какое-то имя', help_text='Ваше имя')
    email = forms.EmailField() # error_messages={'required': 'This field must be filled'}, validators=[]
    text = forms.CharField(widget=forms.Textarea(attrs={'style': 'width:300px;'}))
    # password = forms.CharField(widget=forms.PasswordInput)