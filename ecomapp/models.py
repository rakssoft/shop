from django.db import models
from django.core.files import File
from django.db.models.signals import pre_save
from django.utils.text import slugify
#from transliterate import translit
from django.urls import reverse

from django.utils.safestring import mark_safe

# Create your models here.



class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})

def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_category_slug, sender=Category)


class Brand(models.Model):

    name = models.CharField(max_length=100)
    # slug = models.SlugField(null=True)
    def __str__(self):
        return self.name

def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)

class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available = True)


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    image2 = models.ImageField(upload_to=image_folder)
    indications = models.TextField(null=True)
    contraindications = models.TextField(null=True)
    selection_of_sizes = models.ImageField(upload_to=image_folder, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    available = models.BooleanField(default=True)
    objects = ProductManager()
    instruction_title = models.CharField(max_length=30)
    instruction_pdf = models.FileField(upload_to=image_folder)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1)
    item_tottal = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return "Cart item for product {0}".format(self.product.title)

class Cart(models.Model):
    item = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return str(self.id)

# # class Instruction(models.Model):
# #     instruction_title = models.CharField(max_length=30)
# #     instruction_pdf = models.FileField(upload_to=image_folder)
#
#
#     def __str__(self):
#         return self.instruction_title

class Images(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField()
    image_vk = models.ImageField(upload_to=image_folder)
    image_phone = models.ImageField(upload_to=image_folder)
    image_fb = models.ImageField(upload_to=image_folder)
    image_whatsapp = models.ImageField(upload_to=image_folder)

    def __str__(self):
        return self.title

class MailBox(models.Model):
    class Meta:
        db_table = 'contact_form'
        verbose_name = 'Контактная форма'
        verbose_name_plural = 'Форма обратной связи'

    subject = models.CharField(max_length=20, verbose_name='Имя пользователя')
    sender = models.EmailField(verbose_name='E-mail - пользователя')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    message = models.TextField(max_length=150, verbose_name='Сообщение')
    copy = models.BooleanField()

    def __unicode__(self):
        return self.subject