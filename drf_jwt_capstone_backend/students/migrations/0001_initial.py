# Generated by Django 3.2.8 on 2021-12-08 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('zipcode', models.CharField(blank=True, max_length=5)),
                ('guardian_one', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guardian_one', to=settings.AUTH_USER_MODEL)),
                ('guardian_two', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guardian_two', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
