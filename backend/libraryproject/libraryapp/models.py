from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    avatar = CloudinaryField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Teacher(User):
    active = models.BooleanField(default=False)

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Learning_materials(BaseModel):
    title = models.CharField(max_length=50)
    file = models.FileField()
    
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title
    
class Pay_materials(Learning_materials):
    is_borrowed = models.BooleanField(default=False)
    lisence = models.TextField(max_length=50)

class Rating(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    material = models.ForeignKey(Learning_materials, on_delete=models.CASCADE, null=False)

    comment = models.TextField(max_length=500)

    RATES = {
        1: "1 star",
        2: "2 star",
        3: "3 star",
        4: "4 star",
        5: "5 star",
    }
    rate = models.models.IntegerField(max_length=1, choices=RATES)

class receipt(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    material = models.ForeignKey(Pay_materials, on_delete=models.CASCADE, null=False)
    price = models.IntegerField(null=False)

class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        abstract = True

class Borrow(Interaction):
    material = models.ForeignKey(Pay_materials, on_delete=models.CASCADE, null=False)

class Access(Interaction):
    material = models.ForeignKey(Learning_materials, on_delete=models.CASCADE, null=False)

