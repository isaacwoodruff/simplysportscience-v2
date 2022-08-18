from django import forms
from .models import Job


class JobPostForm(forms.ModelForm):
    '''
    Form for a new job post. The employer field is hidden, then filled in in the view with the logged
    in employer. The slug is hidden and then filled in in the view from the title
    '''
    employment_type = forms.ChoiceField
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(max_length=100, required=True)
    employer = forms.CharField(required=False)
    slug = forms.SlugField(required=False)

    employer.widget = employer.hidden_widget()
    slug.widget = slug.hidden_widget()

    class Meta:
        model = Job
        fields = ["title", "location", "employment_type",
                  "description"]
