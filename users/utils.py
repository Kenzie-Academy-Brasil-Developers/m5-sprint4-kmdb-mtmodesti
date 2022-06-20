from django.contrib.auth.models import BaseUserManager
#sobrescrever base de criação
class CustomUserManager(BaseUserManager):
    def create_super_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError('E-mail must be passed')
        
        email = self.normalize_email(email)
        
        user = self.model(email=email, is_staff=True, is_superuser=True, **extra_fields)
        
        user.save(using=self._db)
        
        return user
    