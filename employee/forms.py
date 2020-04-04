from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=40,min_length=4)
    empno = forms.IntegerField(min_value=1,max_value=1000)
    emailid = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

