# Generated by Django 4.2.3 on 2023-07-31 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Fakultet ismi')),
                ('name_uz', models.CharField(max_length=200, null=True, verbose_name='Fakultet ismi')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Fakultet ismi')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Fakultet ismi')),
                ('link_name', models.CharField(max_length=200, verbose_name='fakultet link')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='F.I.O.')),
                ('birthday', models.DateField(verbose_name="Tug'ilgan kun")),
                ('gender', models.CharField(max_length=10, verbose_name='Jinsi')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Telefon nomer')),
                ('course', models.CharField(blank=True, max_length=20, null=True, verbose_name='Kurs')),
                ('image', models.ImageField(upload_to='./image/', verbose_name='Image')),
                ('i_va_ii', models.FileField(blank=True, null=True, upload_to='./i_va_ii/', verbose_name='I va II guruh nogiron')),
                ('temir_daftar', models.FileField(blank=True, null=True, upload_to='./temir_daftar/', verbose_name='Temir daftar')),
                ('yetim', models.FileField(blank=True, null=True, upload_to='./yetim/', verbose_name='Yetim')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Ariza vaqti')),
                ('is_qabul', models.BooleanField(default=False, verbose_name='Qabul qilindi')),
                ('is_radetildi', models.BooleanField(default=False, verbose_name='Rad etildi')),
                ('commit', models.TextField(blank=True, null=True, verbose_name='Sababi')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.faculties', verbose_name='Fakultet')),
            ],
            options={
                'ordering': ['-create_at'],
            },
        ),
    ]
