from __future__ import unicode_literals
from django.db import models
from ..log_reg.models import User
from datetime import datetime

class ProductManager(models.Manager):
    def validate(self, data):
        errors = []

        if not data["name"]:
            errors.append("Product name is required")
        elif len(data["name"]) < 4:
            errors.append("Product name must be longer than 3 characters")

        response = {}

        if not errors:
            response['added'] = True
        else:
            response['added'] = False
            response['errors'] = errors
        return response

class Product(models.Model):
    name = models.CharField(max_length=50)
    user_products = models.ForeignKey(User, related_name='products_of_user')
    all_users = models.ManyToManyField(User, related_name='all_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()

# Create your models here.
