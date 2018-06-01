from django.db import models


class Categories(models.Model):
    name = models.CharField("Категория", max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Sportsmens(models.Model):
    id = models.IntegerField("Порядковый номер атлета", primary_key=True)
    name = models.CharField("ФИО атлета", max_length=100)
    city = models.CharField("Город, спортивный клуб", max_length=100)
    trener = models.CharField("ФИО тренера", max_length=100)
    category = models.ManyToManyField(Categories, verbose_name="Категория")

    class Meta:
        verbose_name = "Athlete"
        verbose_name_plural = "Athletes"
        ordering = ['id']

    def __str__(self):
        return '%s   |   %s   |   %s' % (self.id, self.name, self.city)
