# Generated by Django 4.2 on 2023-04-20 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_at',
            field=models.DateTimeField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Name'),
        ),
        migrations.CreateModel(
            name='Scoping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.BooleanField(default=False, verbose_name='Main')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.topic', verbose_name='Section')),
            ],
            options={
                'verbose_name': 'Тематика статьи',
                'verbose_name_plural': 'Тематики Статьи',
                'ordering': ['-main', 'tag__name'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='scope',
            field=models.ManyToManyField(through='articles.Scoping', to='articles.topic'),
        ),
    ]
