from django import forms


class FeedbackForm(forms.Form):
    id = forms.IntegerField(label='ID паспорт', )
    author_post = forms.CharField(label='Автор поста')
    title = forms.CharField(label='Заголовок')
    description_post = forms.CharField(label='описание', widget=forms.Textarea(attrs={'style': 'width:300px;'}))
    quantity_likes = forms.IntegerField(label='Количество лайков')
