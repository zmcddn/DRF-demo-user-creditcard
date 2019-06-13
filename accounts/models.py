from datetime import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel


class DynamicMinValueValidator(MinValueValidator):
    """
    Extend from the validator to make a dynamic validator
    """

    def __call__(self, value):
        cleaned = self.clean(value)
        params = {'limit_value': self.limit_value(), 'show_value': cleaned}
        if self.compare(cleaned, self.limit_value()):
            raise ValidationError(
                self.message % params,
                code=self.code,
                params=params,
                )


def current_year():
    # Get current year last two digit
    return int(datetime.now().strftime('%y'))


class Card(TimeStampedModel):
    """
    Databse structure for Credit Card info.

    Note this is a copy and modification from the dj-stripe package
    and it is only used for demo purpose.
    In production we should use dj-stripe for dealing with stripe.
    """

    address_city = models.TextField(
        max_length=5000,
        blank=True,
        default="",
        help_text="City/District/Suburb/Town/Village.",
    )
    address_country = models.TextField(
        max_length=5000, blank=True, default="", help_text="Billing address country."
    )
    address_line1 = models.TextField(
        max_length=5000,
        blank=True,
        default="",
        help_text="Street address/PO Box/Company name.",
    )
    address_line2 = models.TextField(
        max_length=5000,
        blank=True,
        default="",
        help_text="Apartment/Suite/Unit/Building.",
    )
    address_state = models.TextField(
        max_length=5000,
        blank=True,
        default="",
        help_text="State/County/Province/Region.",
    )
    address_zip = models.TextField(
        max_length=5000, blank=True, default="", help_text="ZIP or postal code."
    )
    country = models.CharField(
        max_length=2,
        default="",
        blank=True,
        help_text="Two-letter ISO code representing the country of the card.",
    )
    exp_month = models.PositiveSmallIntegerField(
        help_text="Card expiration month.",
        validators=[MinValueValidator(1), MaxValueValidator(12)],
    )
    exp_year = models.PositiveSmallIntegerField(
        help_text="Card expiration year.",
        validators=[DynamicMinValueValidator(current_year()), MaxValueValidator(99)],
    )
