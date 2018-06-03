from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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
    city = models.CharField("Город", max_length=50)
    trener = models.CharField("ФИО тренера", max_length=100)
    category = models.ManyToManyField(Categories, verbose_name="Категория")

    class Meta:
        verbose_name = "Athlete"
        verbose_name_plural = "Athletes"
        ordering = ['id']

class SportsmensSportsmensCategory(models.Model):
    id = models.IntegerField("id", primary_key=True)
    sportsmens = models.ForeignKey(Sportsmens, models.DO_NOTHING)
    categories = models.ForeignKey(Categories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sportsmens_sportsmens_category'
        unique_together = (('sportsmens', 'categories'),)



class Rating(models.Model):
    position = models.IntegerField('Место')
    user = models.ForeignKey(
        User,
        verbose_name="Оценивающий судья",
        on_delete=models.CASCADE
    )
    sportsmen_category = models.ForeignKey(
        SportsmensSportsmensCategory,
        verbose_name="Оцениваемый спортсмен",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
