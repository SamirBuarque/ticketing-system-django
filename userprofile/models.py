from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

    # adiciona automaticamente a data de criação desse usuario
    #created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now)

    """ Armazenar no banco de dados o hash gerado """
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    
