# Generated by Django 3.1.2 on 2020-11-28 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app', '0005_auto_20201116_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author'),
        ),
        migrations.AlterField(
            model_name='likedislike',
            name='content_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='likedislike',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='likedislike',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='likedislike',
            name='vote',
            field=models.SmallIntegerField(choices=[(-1, 'Не нравится'), (1, 'Нравится')], default=0, verbose_name='Голос'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=256, unique=True, verbose_name='Тэг'),
        ),
        migrations.AlterUniqueTogether(
            name='likedislike',
            unique_together={('user', 'content_type', 'object_id')},
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
