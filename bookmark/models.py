from django.db import models

class WebSite(models.Model):
    siteName = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    
    def __str__(self): #매직 메서드
        return "이름 : " + self.siteName + ", 주소 : " + self.url