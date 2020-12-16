# Generated by Django 3.1.2 on 2020-11-17 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='이름')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='등록')),
            ],
        ),
    ]
