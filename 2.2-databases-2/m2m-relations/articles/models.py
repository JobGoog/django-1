from django.db import models



class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Name')
    text = models.TextField(verbose_name='Text')
    published_at = models.DateTimeField(verbose_name='Data')
    image = models.ImageField(null=True, blank=True, verbose_name='Image', )
    scope = models.ManyToManyField(Topic, through='Scoping')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scoping(models.Model):
    tag = models.ForeignKey(Topic, on_delete=models.CASCADE,
                            verbose_name='Section')
    main = models.BooleanField(default=False, verbose_name='Main')
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='scopes')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики Статьи'
        ordering = ['-main', 'tag__name']
