from django import forms

from .models import FunFactSubmission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = FunFactSubmission
        fields = ['username', 'fun_fact']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fun_fact': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '5'
                }
            )
        }