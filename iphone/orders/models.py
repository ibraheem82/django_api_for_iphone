from distutils.command.upload import upload
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


User = get_user_model()


class Order(models.Model):
    TYPES = (
        ('IPhone SE (1ST GENERATION)', 'iphone se (1st generation)'),
        ('IPhone 6', 'iphone 6'),
        ('IPhone 6 PLUS', 'iphone 6 plus'),
        ('IPhone 6s', 'iphone 6s'),
        ('IPhone 7', 'iphone 7'),
        ('IPhone 7 PLUS', 'iphone 7 plus'),
        ('IPhone 8', 'iphone 8'),
        ('IPhone 8 PLUS', 'iphone 8 plus'),
        ('IPhone X', 'iphone x'),
        ('IPhone XR', 'iphone Xr'),
        ('IPhone XS MAX', 'iphone Xs Max'),
        ('IPhone XS', 'iphone Xs'),
        ('IPhone SE (2ND GENERATION)', 'iphone se (2nd generation'),
        ('IPhone 11', 'iphone 11'),
        ('IPhone 11 PRO MAX', 'iphone 11 Pro Max'),
        ('IPhone 11 PRO', 'iphone 11 Pro'),
        ('IPhone 12', 'iphone 12'),
        ('IPhone 12 MINI', 'iphone 12 mini'),
        ('IPhone 12 PRO', 'iphone 12 Pro'),
        ('IPhone SE (3RD GENERATION)', 'iphone se(3rd generation)'),
        ('IPhone 13 MINI', 'iphone 13 mini'),
        ('IPhone 13', 'iphone 13'),
        ('IPhone 13 PRO MAX', 'iphone 13 Pro Max'),
        ('IPhone 13 PRO', 'iphone 13 Pro'),
        
        )
    ORDER_STATUS = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'inTransit'),
        ('DELIVERED', 'delivered'),
    )
    
    # PHONE_COLORS = (
    #     ('ALPINE GREEN', 'alpine green'),
    #     ('SILVER', 'silver'),
    #     ('GOLD', 'gold'),
    #     ('GRAPHITE', 'graphite'),
    #     ('SIERRA BLUE', 'sierra blue'),
    # )
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # phone_images = models.ImageField(upload_to = "images", null=True)
    # phone_colors = models.CharField(max_length=20, choices=PHONE_COLORS, default=PHONE_COLORS[1][0])
    # decription = models.TextField(null=True)
    iphone_types = models.CharField(max_length=40, choices=TYPES, default=TYPES[0][0])
    order_status = models.CharField(max_length = 40, choices=ORDER_STATUS, default = ORDER_STATUS[0][0])
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    
    
    def __str__(self):
        return f"<Order {self.iphone_types} by {self.customer.id}>"
