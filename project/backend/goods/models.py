from django.db import models
from services.models import Service


class Good(models.Model):
    title = models.CharField(max_length=254, verbose_name="Название")
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена")
    price_coefficient = models.DecimalField(
        max_digits=5, decimal_places=2, default=0, verbose_name="Ценовой коэффициент"
    )
    related_products = models.ManyToManyField("self", blank=True, verbose_name="Сопутствующие товары")
    mandatory_services = models.ManyToManyField(Service, blank=True, verbose_name="Обязательные услуг")
    available = models.BooleanField(default=True, verbose_name="Есть ли в наличии")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
