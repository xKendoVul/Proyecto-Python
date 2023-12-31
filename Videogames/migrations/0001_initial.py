# Generated by Django 4.2.7 on 2023-11-13 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Platforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('user_image', models.ImageField(upload_to='Videogames/images/users')),
            ],
        ),
        migrations.CreateModel(
            name='Games_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_image', models.ImageField(upload_to='Videogames/images/games')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('date_sale', models.DateField()),
                ('votes', models.IntegerField(default=0)),
                ('game_time', models.TimeField()),
                ('genre', models.ManyToManyField(to='Videogames.genres')),
                ('platforms', models.ManyToManyField(to='Videogames.platforms')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment_text', models.CharField(max_length=500)),
                ('date_published', models.DateTimeField()),
                ('id_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Videogames.games_data')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Videogames.users')),
            ],
        ),
    ]
