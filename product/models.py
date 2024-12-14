from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    url = models.URLField(null=True, blank=True)  # Ссылка на продукт
    main_photo = models.URLField(null=True, blank=True)  # Ссылка на изображение из интернета

    def __str__(self):
        return self.name
