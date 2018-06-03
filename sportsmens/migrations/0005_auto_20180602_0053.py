# Generated by Django 2.0.5 on 2018-06-01 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsmens', '0004_auto_20180602_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportsmensSportsmensCategory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
            ],
            options={
                'db_table': 'sportsmens_sportsmens_category',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='sportsmens_and_category',
            name='categories_id',
        ),
        migrations.RemoveField(
            model_name='sportsmens_and_category',
            name='sportsmens_id',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='sportsmen',
        ),
        migrations.DeleteModel(
            name='Sportsmens_and_category',
        ),
        migrations.AddField(
            model_name='rating',
            name='sportsmen_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sportsmens.SportsmensSportsmensCategory', verbose_name='Оцениваемый спортсмен'),
            preserve_default=False,
        ),
    ]