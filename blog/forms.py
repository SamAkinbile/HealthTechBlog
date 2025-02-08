from .models import Comment
from django import forms
from .models import Contact
from .models import NewsletterSubscription

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)



class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']