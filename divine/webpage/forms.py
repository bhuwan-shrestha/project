from django import forms
from webpage.models import ContactUs

class ContactUsForm(forms.ModelForm):
	class Meta:
		model = ContactUs
		exclude = ('date',)

	def __init__(self, *args, **kwargs):
		super(ContactUsForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget = forms.TextInput(attrs={
			'placeholder': 'Full Name',
			})
		self.fields['email'].widget = forms.EmailInput(attrs={
			'placeholder': 'Email',
			})
		self.fields['city'].widget = forms.TextInput(attrs={
			'placeholder': 'City',
			})
		self.fields['state'].widget = forms.TextInput(attrs={
			'placeholder': 'State',
			})
		self.fields['message'].widget = forms.Textarea(attrs={
			'placeholder': 'Message',
			})