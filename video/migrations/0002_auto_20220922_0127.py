# Generated by Django 3.1.3 on 2022-09-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ManyToManyField(blank=True, default=None, related_name='category', to='video.Category'),
        ),
    ]
