# Generated by Django 4.2.7 on 2023-11-01 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universidad', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='facultades/logos/')),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='programas/logos/')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_programas', to='university.facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('formacion', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='docentes/')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_docentes', to='university.programa')),
            ],
        ),
    ]