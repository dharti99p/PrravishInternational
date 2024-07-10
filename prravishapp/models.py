from django.db import models


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    interested_product = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# products

class MenuStarter(models.Model):
    image = models.ImageField(upload_to=('Menu'))
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuMain(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuDrinks(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuOffers(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuSpecial(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)

