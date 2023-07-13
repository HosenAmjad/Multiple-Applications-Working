
from django.db import models

class signupUser(models.Model):
    firstName = models.CharField(max_length=50, blank=False, null=False)
    lastName = models.CharField(max_length=50, blank=False, null=False)
    userName = models.CharField(max_length=100, blank=False, null=False)
    userTitle = models.CharField(max_length=250, blank=False, null=False)
    gender = models.CharField(max_length=15, blank=False, null=False)
    dateofBirth = models.DateTimeField(auto_now=False, auto_now_add=True)
    email = models.CharField(max_length=80, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    mobile = models.CharField(blank=True, null=False, default="000 00000 000000")
    region = models.CharField(max_length=20, blank=True, null=False)
    address = models.TextField(max_length=250, blank=True, null=False)
    city = models.CharField(max_length=100, blank=True, null=False)
    postalcode = models.CharField(max_length=12, blank=True, null=False)
    country = models.CharField(max_length=100, blank=True, null=False)
    website = models.CharField(max_length=250, blank=True, null=False)
    picture = models.ImageField(upload_to="profile/", blank=True, null=False)
    Description = models.TextField(max_length=500, blank=True, null=False)
    slug = models.SlugField(default="", null=False)
    status = models.BooleanField(default=False)
    
    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)


    class Meta:
            verbose_name = "signupUser"
            verbose_name_plural = "New User"

    def __str__(self):
        return f'0{self.id}'
