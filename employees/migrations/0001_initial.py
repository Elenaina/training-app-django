# Generated by Django 2.2.3 on 2019-07-10 11:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=200)),
                ('position_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('employed_since', models.DateTimeField(default=django.utils.timezone.now)),
                ('sallary', models.DecimalField(decimal_places=2, max_digits=19)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('is_present', models.BooleanField()),
                ('leave_left', models.IntegerField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.Position')),
            ],
        ),
    ]
