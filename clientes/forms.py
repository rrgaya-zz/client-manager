from django.forms import ModelForm
from .models import Person

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))