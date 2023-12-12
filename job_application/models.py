from django.db import models


class Form(models.Model):
    """
    A class representing a form.

    Attributes:
        first_name (CharField): The first name of the form.
        last_name (CharField): The last name of the form.
        email (EmailField): The email address of the form.
        date (DateTimeField): The date of the form.
        occupation (CharField): The occupation of the form.
    """

    first_name = models.CharField(
        max_length=80,
        help_text="Enter your first name.",
        verbose_name="First Name",
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=80,
        help_text="Enter your last name.",
        verbose_name="Last Name",
        blank=False,
        null=False,
    )
    email = models.EmailField(
        help_text="Enter your email address.",
        verbose_name="Email",
        unique=True,
        blank=False,
        null=False,
    )
    date = models.DateTimeField(
        auto_now_add=True,
        help_text="Select a date.",
        verbose_name="Date",
        blank=False,
        null=False,
    )
    occupation = models.CharField(
        max_length=80,
        help_text="Enter your occupation.",
        verbose_name="Occupation",
        blank=False,
        null=False,
    )

    def __str__(self):
        """
        Returns a string representation of the form.

        Returns:
            str: The concatenation of the first name and last name.
        """
        return f"{self.first_name} {self.last_name}"
