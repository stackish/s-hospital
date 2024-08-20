# Generated by Django 4.2.8 on 2024-03-18 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=100, null=True)),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
