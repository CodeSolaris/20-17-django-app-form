from django import forms


class ApplicationForm(forms.Form):
    """
    A Django form used to collect and validate user input for a job application.

    Fields:
    - first_name: a character field with a maximum length of 80 characters, used to collect the applicant's first name
    - last_name: a character field with a maximum length of 80 characters, used to collect the applicant's last name
    - email: an email field, used to collect the applicant's email address
    - date: a date field, used to collect the date of the application
    - occupation: a character field with a maximum length of 80 characters, used to collect the applicant's occupation
    """

    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)
