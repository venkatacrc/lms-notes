from django import forms

class NoteForm(forms.Form):
    captured_note = forms.CharField(label='',widget=forms.Textarea)
