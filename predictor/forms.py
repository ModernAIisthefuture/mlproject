from django import forms

class BostonForm(forms.Form):
    CRIM = forms.FloatField()
    ZN = forms.FloatField()
    INDUS = forms.FloatField()
    CHAS = forms.FloatField()
    NOX = forms.FloatField()
    RM = forms.FloatField()
    AGE = forms.FloatField()
    DIS = forms.FloatField()
    RAD = forms.FloatField()
    TAX = forms.FloatField()
    PTRATIO = forms.FloatField()
    B = forms.FloatField()
    LSTAT = forms.FloatField()
