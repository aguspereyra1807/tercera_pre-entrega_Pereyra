# Generated by Django 4.2.3 on 2023-08-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstrumentsApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.AddField(
            model_name='branch',
            name='province',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
