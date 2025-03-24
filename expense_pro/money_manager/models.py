from django.db import models

# Create your models here. 


categories={
        ('Travel','Travel'),
        ('Entertainment','Entertainment'),
        ('Food','Food'),
        ('Hospital','Hospital'),
        ('Education','Education'),
        ('Shopping','Shopping'),
        ('Necessities','Necessities'),
        ('Others','Others'),
}
class Expense(models.Model):
    category=models.CharField(max_length=100,choices=categories,default=None)
    date=models.DateTimeField(auto_now_add=False,auto_now=False)
    description=models.TextField(max_length=300)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
