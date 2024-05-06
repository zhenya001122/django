from django import forms
from .models import Category, Husband, Women
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категории')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Не замужем', required=False, label='Муж')

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'husband', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина первышает 50 симолов')

        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')
