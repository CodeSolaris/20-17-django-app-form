from django.contrib import messages
from django.shortcuts import redirect, render

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
            messages.success(request, "Form submitted successfully")
            return redirect("index")

    return render(request, "index.html")
