from django.db import models
from django.contrib.auth.models import User


class mensajeria(models.Model):
    emisor=models.ForeignKey(User, on_delete=models.CASCADE)
    #receptor=models.ForeignKey("", on_delete=models.CASCADE)
    cuerpo=models.TextField(max_length=50)
    leido=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.emisor+" "+self.cuerpo+" "+self.leido
