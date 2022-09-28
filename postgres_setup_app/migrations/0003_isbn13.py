# Generated by Django 3.2 on 2022-09-16 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postgres_setup_app', '0002_bookclub'),
    ]

    operations = [
        migrations.CreateModel(
            name='ISBN13',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=17)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='postgres_setup_app.book')),
            ],
        ),
    ]
