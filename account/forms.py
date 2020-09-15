from django import forms

class Radio(forms.Form):
    CHOICES=[('teacher','Teacher'),('student','Student')]

    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

