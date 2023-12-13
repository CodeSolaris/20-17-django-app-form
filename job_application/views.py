from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from .forms import ApplicationForm
from .models import Form


def index(request):
    """
    Handles a POST request, validates the form data, saves it to the database, and displays a success message.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML template.
    """
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            Form.objects.create(**form.cleaned_data)
            message_body = f"""
                A new job application has been submitted:
                Thank you for your interest {form.cleaned_data["first_name"]}
                {form.cleaned_data["date"]}
                """
            email_message = EmailMessage(
                "Form Submission confirmation",
                message_body,
                to=[form.cleaned_data["email"]],
            )
            email_message.send()
            messages.success(request, "Form submitted successfully")
            return redirect("index")

    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


