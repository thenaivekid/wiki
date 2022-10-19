import re
from .util import list_entries

from django import forms


class NewPageForm(forms.Form):
    """Form to create new page."""

    title = forms.CharField(
        max_length=100,
        required=True
    )

    entry = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def clean_title(self):
        """Validate if title exists."""

        title = self.cleaned_data.get('title')
        if title in list_entries():
            raise forms.ValidationError('Name exists. Take another.')

        return title

    


class EditPageForm(NewPageForm):
    """Form for edit existing entries."""

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title

    
