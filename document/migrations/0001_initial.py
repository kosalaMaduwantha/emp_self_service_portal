# Generated by Django 4.1.4 on 2023-01-08 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_doc', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('uploaded_date', models.DateField()),
                ('updated_date', models.DateField()),
                ('document_category', models.CharField(max_length=40)),
                ('doc_link', models.CharField(max_length=300)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
