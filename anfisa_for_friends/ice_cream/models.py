from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(
        default=100, verbose_name='Порядок отображения')


class Topping(PublishedModel):
    slug = models.SlugField(max_length=64, unique=True)


class Wrapper(PublishedModel):
    ...


class IceCream(PublishedModel):
    description = models.TextField()
    output_order = models.PositiveSmallIntegerField(
        default=100, verbose_name='Порядок отображения')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
    )
    toppings = models.ManyToManyField(Topping)
    is_on_main = models.BooleanField(default=False)
