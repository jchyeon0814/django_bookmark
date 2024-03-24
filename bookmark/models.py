from django.db import models

class WebSite(models.Model):
    siteName = models.CharField(max_length=100)
    url = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.siteName