# Generated by Django 4.1.2 on 2022-10-20 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_alter_department_dept_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='root.institution'),
        ),
    ]
