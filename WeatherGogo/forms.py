from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Enter the city'
    })}

# class UserForm(forms.Form):
#     username = forms.CharField(label="Username")
#     age = forms.IntegerField(label="Age")
#     email = forms.EmailField(label="Email")
#     password = forms.CharField(min_length=5, max_length=10)

# class OutfitForm(forms.Form):
    # weather = forms.IntegerField(max_value=50, min_value=-50, step_size=1, required=False, label="Weather")
    # age = forms.IntegerField(max_value=100, min_value=14, step_size=1)
    # mood = forms.ChoiceField(choices=((1, "Bad"), (2, "Good"), (3, "Calm"), (4, "Super")), label="Mood")
    # clothes = forms.CheckboxSelectMultiple()
    # grunge = forms.CheckboxSelectMultiple()
    # classic = forms.CheckboxSelectMultiple()
    # casual = forms.CheckboxSelectMultiple()
    # romantic = forms.CheckboxSelectMultiple()
    # sport = forms.CheckboxSelectMultiple()
    # glamour = forms.CheckboxSelectMultiple()
    # retro = forms.CheckboxSelectMultiple()