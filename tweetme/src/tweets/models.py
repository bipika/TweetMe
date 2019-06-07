from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

from .validators import validate_content


class Tweet(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    content=models.CharField(max_length=100,validators=[validate_content])
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    # def clean(self,*args,**kwargs):
    #     content=self.cleaned_data.get("content")
    #     if content=="abc":
    #         raise ValidationError("Cannot be ABC")
    #     return content
    def get_absolute_url(self):
        return reverse("tweet:detail",kwargs={"pk":self.pk})