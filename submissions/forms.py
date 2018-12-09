from django import forms

from .models import Submission



class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('visible_title', 'content', 'perp_name', 'place')

# visible_title = forms.CharField(label='Visible Title (for your own reference)', max_length=100)
# content = forms.CharField(label='Add a Description')
# perp_name = forms.CharField(label='What is their name?', max_length=100)
# place = forms.CharField(label='What are relevant places?', max_length=100)