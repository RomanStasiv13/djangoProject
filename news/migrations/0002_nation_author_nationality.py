# Generated by Django 4.0.4 on 2022-04-30 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='nationality',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='news.nation'),
        ),
    ]
