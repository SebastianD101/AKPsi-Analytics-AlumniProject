from django import forms
from .models import Alumni

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['name', 'linkedin', 'email', 'graduation_date', 'majors', 'sphere', 'position', 'current_company', 'location', 'previous_companies']
        labels = {
            'name': 'Full Name',
            'graduation_date': 'Graduation Year',
            'current_company': 'Current Employer',
            'previous_companies': 'Previous Employers & Positions',
            'linkedin': 'LinkedIn URL'
        }
        required = {
            'email': False
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['majors'].widget = forms.TextInput(attrs={'placeholder': 'Enter comma-separated list of majors'})
        self.fields['previous_companies'].widget = forms.Textarea(attrs={'rows': 3})
