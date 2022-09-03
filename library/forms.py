from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    # picture = forms.ImageField(
    #     widget=forms.FileInput,
    # )

    class Meta:
        model = Book
        fields = (
            'title',
            'description',
            'picture',
            'year',
        )
        labels = {
            'title': 'Название книги',
            'description': 'Описание книги',
            'picture': 'Обложка',
            'year': 'Год написания',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title'),
                Column('year'),
            ),
            Row(
                Column('description'),
            ),
            FieldWithButtons(
                'picture',
                StrictButton('Загрузить', type='submit', css_class='btn btn-primary'),
            ),
            Submit('submit', 'Сохранить', css_class='btn btn-primary btn-lg btn-block'),
        )
