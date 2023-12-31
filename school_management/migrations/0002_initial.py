# Generated by Django 4.2.3 on 2023-07-18 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.school'),
        ),
        migrations.AddField(
            model_name='document',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.application'),
        ),
        migrations.AddField(
            model_name='application',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.school'),
        ),
    ]
