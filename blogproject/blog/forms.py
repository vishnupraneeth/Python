from django import forms
class EmailSendForms(forms.Form):
     name=forms.CharField()
     Email=forms.EmailField()
     to=forms.EmailField()
     comments=forms.CharField(required=False,widget=forms.Textarea)
