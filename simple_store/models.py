from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
import datetime

class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=255)
    description = models.TextField(_("Category Description"))
    slug = models.SlugField(_("Category Slug"), db_index=True)
    active = models.BooleanField(_("Active"), default=True, db_index=True)

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Category, self).save(**kwargs)

class Product(models.Model):
    name = models.CharField(_("Product Name"), max_length=255)
    description = models.TextField(_("Product Description"))
    category = models.ManyToManyField(Category, blank=True, verbose_name=_("Product Category"))
    slug = models.SlugField(_("Product Slug"), blank=True)
    sku = models.CharField(_("Product SKU"), max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(_("Quantity"), default=0)

    active = models.BooleanField(_("Active"), default=True, db_index=True)
    feature = models.BooleanField(_("Featured"), default=False, db_index=True)

    created = models.DateTimeField(_("Created"), blank=True)
    updated = models.DateTimeField(_("Updated"), blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        if not self.pk:
            self.created = datetime.datetime.today()

        if not self.slug:
            self.slug = slugify(self.name)

        if not self.sku:
            self.sku = self.slug

        super(Product, self).save(**kwargs)
