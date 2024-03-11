# Generated by Django 5.0.2 on 2024-03-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tesera_id', models.IntegerField()),
                ('tesera_name', models.CharField(max_length=1024)),
                ('tesera_rating_user', models.FloatField()),
                ('tesera_n10_rating', models.FloatField()),
                ('bgg_id', models.IntegerField()),
                ('bgg_name', models.CharField(max_length=1024)),
                ('bgg_average_rating', models.FloatField()),
                ('bgg_bayes_average_rating', models.FloatField()),
                ('bgg_rank', models.IntegerField()),
                ('bgg_weight', models.FloatField()),
            ],
        ),
    ]