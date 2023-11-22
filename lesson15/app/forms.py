from django import forms
from django.core.exceptions import ValidationError

from .models import Course


def check_number_validator(value):
    for ch in value:
        if ch.isdigit():
            raise ValidationError(message='There are numbers in title!')


# Обычная форма
class CourseCreateForm(forms.Form):
    title = forms.CharField(validators=[check_number_validator])
    description = forms.CharField(widget=forms.Textarea())
    avg_time = forms.IntegerField()


# Форма на основе модели
class CourseCreateModelForm(forms.ModelForm):
    # title = forms.IntegerField() # переопределение

    class Meta:
        model = Course
        fields = '__all__'
        # fields = ('title', 'description',)
        # exclude = ('title',)
        labels = {'title': 'Название курса',}
        # widgets = {'title': forms.NumberInput()}
