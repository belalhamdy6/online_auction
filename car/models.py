from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify



# Create your models here.
Car_TYPE = (
    ("sedan", "sedan"),
    ("hatchBack", "hatchBack"),
    ("coupe", "coupe"),
    ("crossover", "crossover"),
)
transmission = (
    ("Automatic", "Automatic"),
    ("manual", "manual"),
)
Bid_on = (
    ("On_Bid", "On_Bid"),
    ("Coming_Soon", "Coming_Soon"),


)
Category = (
    ("New", "New"),
    ("Used", "Used"),
    ("Crashed", "Crashed"),

)

def image_upload(instance, filename):
    imagename , extension = filename.split(".")
    return "car/%s.%s"%(instance.id, extension)

class Job(models.Model):
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    model_car = models.IntegerField(default=1900)
    car_type = models.CharField(max_length=15, choices=Car_TYPE)
    city = models.ForeignKey('City_car', related_name='car_city', on_delete=models.CASCADE, blank=True, null=True)
    descreption = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    mileage = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    engine = models.IntegerField(default=1)
    bid_on = models.CharField(max_length=30, choices=Bid_on)
    color = models.CharField(max_length=15)
    Category = models.CharField(max_length=50, choices=Category)
    transmission = models.CharField(max_length=20, choices=transmission)
    image = models.ImageField(upload_to=image_upload, blank=True, null=True)
    image_a = models.ImageField(upload_to=image_upload, blank=True, null=True)
    image_b = models.ImageField(upload_to=image_upload, blank=True, null=True)
    image_c = models.ImageField(upload_to=image_upload, blank=True, null=True)
    image_d = models.ImageField(upload_to=image_upload, blank=True, null=True)
    image_e = models.ImageField(upload_to=image_upload, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



class Apply_For(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)

    name  =    models.CharField(max_length=50)
    email =    models.EmailField(max_length=30)
    link  =    models.URLField()
    cv    =    models.FileField(upload_to='apply')
    coverL = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class City_car(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return str(self.name)


class Bid_price(models.Model):
    owner_bid = models.ForeignKey(User, related_name='owner_bid', on_delete=models.CASCADE, null=True, blank=True)
    bid_price = models.IntegerField()

    def __str__(self):
        return str(self.bid_price)


