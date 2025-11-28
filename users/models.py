from django.db import models

class LoginData(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)  # Production me password hash karo

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
