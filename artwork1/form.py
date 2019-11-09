from django import forms


class Comment_Form(forms.Form):
    comment = forms.CharField(required=True, widget=forms.Textarea)