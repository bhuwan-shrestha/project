from django.db import models

# Create your models here.

### Home models ###
class BannerImage(models.Model):
    banner_image = models.ImageField(blank=False, null=False)

class FeatureName(models.Model):
    house_name = models.CharField(max_length=150)
    image = models.ImageField(blank=False, null=False)
    dimention = models.CharField(max_length=60)
    beds = models.PositiveIntegerField()
    bath = models.PositiveIntegerField()
    width= models.CharField(max_length=60)
    depth = models.CharField(max_length=60)

    def __str__(self):
        return self.house_name

class HomeChoose(models.Model):
    image = models.ImageField(blank=False, null=False)
    title = models.CharField(max_length=120)
    describe = models.TextField(max_length=230)

    def __str__(self):
        return self.title

class HomeService(models.Model):
    image = models.ImageField(blank=False, null=False)
    title = models.CharField(max_length=120)
    describe = models.TextField(max_length=430)

    def __str__(self):
        return self.title

class ActionBtn(models.Model):
    action_title = models.CharField(max_length=100)


class Testimonial(models.Model):
    image = models.ImageField(blank=False, null=False)
    name = models.CharField(max_length=60)
    company = models.CharField(max_length=60)
    describe = models.TextField(max_length=250)

    def __str__(self):
        return self.name

#### base social network

class Social(models.Model):
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    googleplus = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)


### About Us models ###

class AboutBanner(models.Model):
    image = models.ImageField(blank=False)

class AboutDetails(models.Model):
    image = models.ImageField(blank=False)
    describe = models.TextField(blank=False)

class OurTeam(models.Model):
    name = models.CharField(max_length=60, blank=False)
    position = models.CharField(max_length=60, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    profile = models.ImageField(blank=True)

    def __str__(self):
        return self.name

### Service models ###

class ServiceBanner(models.Model):
    image = models.ImageField(blank=False)

class ServiceDetails(models.Model):
    image = models.ImageField(blank=False)
    title = models.CharField(max_length=100, blank=False)
    describe = models.TextField(blank=False)

    def __str__(self):
        return self.title

### feature collection ###

class FeatureCollection(models.Model):
    image = models.ImageField(blank=False)

### contact us ###

class ContactBanner(models.Model):
    image = models.ImageField(blank=False)

class OfficeAddress(models.Model):
    address = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return self.address

class OfficeNumber(models.Model):
    telephone = models.PositiveIntegerField(blank=True)
    mobile = models.PositiveIntegerField(blank=False)

class WorkingHours(models.Model):
    working_day = models.CharField(blank=False, max_length=100)
    holiday = models.CharField(blank=False, max_length=100)

class ContactUs(models.Model):

    name = models.CharField(max_length=60, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    message = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

### Inner Feature Section ####

class InnerFeature(models.Model):
    slide_image = models.ImageField(blank=False)
    about_project = models.TextField (blank=False)

class AuthorName(models.Model):
    name = models.CharField(max_length=60, blank=False)
    work = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name

class HouseDimenssion(models.Model):
    title = models.CharField(max_length=60, blank=False)
    area = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.title


