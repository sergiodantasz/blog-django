# Generated by Django 4.2.5 on 2023-10-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('show_header', models.BooleanField(default=True)),
                ('show_search', models.BooleanField(default=True)),
                ('show_menu', models.BooleanField(default=True)),
                ('show_description', models.BooleanField(default=True)),
                ('show_pagination', models.BooleanField(default=True)),
                ('show_footer', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Setup',
                'verbose_name_plural': 'Setups',
            },
        ),
    ]
