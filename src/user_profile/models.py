from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class UserProfile(models.Model):
    user            = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name       = models.CharField(max_length=100)
    gender          = models.CharField(max_length=10)
    nationality     = models.CharField(max_length=50)
    religion        = models.CharField(max_length=50)
    marital_status  = models.CharField(max_length=20)
    health_info     = models.TextField()
    height          = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight          = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    blood_type      = models.CharField(max_length=5)
    criminal_record = models.TextField()
    children_data   = models.TextField()
    id_card_image   = models.ImageField(upload_to='id_card_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username

