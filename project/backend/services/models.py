from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=254, verbose_name="Название")
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
