# Generated by Django 3.0.5 on 2020-04-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namalengkap', models.CharField(max_length=50, null=True)),
                ('nis', models.CharField(max_length=10, null=True)),
                ('kelas', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]