# Generated by Django 4.1.2 on 2022-10-20 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='root.department'),
        ),
    ]
