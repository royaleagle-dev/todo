# Generated by Django 2.2.15 on 2020-08-13 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('d', 'done'), ('nd', 'Not Done')], default='nd', max_length=2)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
