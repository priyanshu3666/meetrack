# Generated by Django 3.2 on 2021-04-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_contact_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]