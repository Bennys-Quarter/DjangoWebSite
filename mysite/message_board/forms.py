from django import forms
from .models import Entry
# Remember: form variable and id have to be identical
# Remember: <label for="name_a"></label>
# Remember: <input  type="text" name="name_a" id="name_a" maxlength="100" required/>
# Remember: the fields for=... ; name=... ; id=... must be identical

class NameForm(forms.Form):
    name_a = forms.CharField(label='your_name', max_length=100)
    name_b = forms.CharField(label='receiver_name', max_length=100)
    msg = forms.CharField(label="message_name", max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;'}))

class Testing(forms.Form):
    name_a = forms.CharField(label='Your name', max_length=100)
