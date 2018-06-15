from django import forms

class ContactForm(forms.Form):

    full_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Full Name'
        }
    ),
        required=True
    )

    email_address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Email Address'
        }
    ),
        required=True
    )

    comments = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-input',
            'placeholder': 'Comments'
        }
    ),
        required=True,
        max_length=400,
    )
