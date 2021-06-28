from django import forms
from .models import File


class FileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = '__all__'

    def clean_name(self):
        file_name = self.cleaned_data['name']
        dot_index = str(file_name).index('.')
        extension = str(file_name)[(dot_index + 1):]
        if extension == 'pdf':
            return file_name
        raise forms.ValidationError('Only pdf files are allowed')
