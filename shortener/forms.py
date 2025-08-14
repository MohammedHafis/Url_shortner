
from django import forms

class URLForm(forms.Form):
    long_url = forms.URLField(label="Long URL", widget=forms.URLInput(attrs={
        "class": "form-control form-control-lg",
        "placeholder": "https://example.com/very/long/link"
    }))
    custom_code = forms.CharField(
        label="Custom short code (optional)",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "e.g., my-link (3–20 chars)"
        }),
        help_text="Letters, numbers, '-' and '_' allowed."
    )
