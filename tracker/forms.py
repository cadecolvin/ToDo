from django import forms

class ItemForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50)
    description = forms.CharField(label='Description', max_length=128)

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
