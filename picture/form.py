from django import forms


class Comment_Form(forms.Form):
    """ Create a text area for users to leave comments """
    comment = forms.CharField(required=True, widget=forms.Textarea)