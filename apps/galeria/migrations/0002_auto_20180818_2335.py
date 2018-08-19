# Generated by Django 2.0.8 on 2018-08-18 23:35

import apps.galeria.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('src', models.ImageField(upload_to=apps.galeria.models.update_filename)),
                ('tags', tagging.fields.TagField(blank=True, max_length=255, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]