# Generated by Django 2.1.7 on 2019-09-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boot',
            name='bt_class',
            field=models.CharField(choices=[('U', 'U'), ('UB', 'UB'), ('UC', 'UC')], max_length=10, verbose_name='uboot class'),
        ),
    ]