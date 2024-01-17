from django import forms

class NewEntryForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    content = forms.CharField(widget=forms.Textarea)

class EntryEditionForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

