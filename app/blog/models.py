from django.db import models

from utils.randoms import new_slugify


class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=255
    )
    is_published = models.BooleanField(
        default=False, help_text='If this field is checked, the page will be displayed publicly.'
    )
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
