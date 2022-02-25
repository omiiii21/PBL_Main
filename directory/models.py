from django.db import models
from django.contrib.auth.models import User

class Directory (models.Model):
 
    Name = models.TextField()
    Number = models.TextField()
    Email = models.EmailField(max_length=254)
    Position = models.TextField()
    
    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.Name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
