# Generated by Django 3.0.7 on 2020-06-19 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_answer_favorited_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='tags',
            field=models.ManyToManyField(related_name='answers', to='core.Tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='questions', to='core.Tag'),
        ),
    ]
