# Generated by Django 3.1.2 on 2020-11-13 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Имя')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Авторы',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статья',
            },
        ),
    ]
