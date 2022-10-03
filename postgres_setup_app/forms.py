from django import forms
from django.core.mail import send_mail

from .models import Book, Author
from .tasks import send_feedback_email_task




class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name',)


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author',)


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )
