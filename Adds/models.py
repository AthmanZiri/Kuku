# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
'''
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
   # company = models.CharField(max_length=50, blank=True)
'''

class Adds(models.Model):
	title=models.CharField(max_length=70, null=True)
	choose_category = models.CharField(max_length=50, choices= (
		(u'Broilers', u'Broilers',), 
		(u'Layers', u'Layers'), 
		(u'Kenbro', u'Kenbro'),
		(u'Kienyeji', u'Kienyeji'),
		(u'Hybreed', u'Hybreed'),
		(u'Kuroiler', u'Kuroiler'),
		(u'Rainbow Rooster', u'Rainbow Rooster'),
		(u'Chicken Feed', u'Chicken Feed'),
		(u'Eggs', u'Eggs')),
		 null=True)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	quantity=models.CharField(max_length=4)
	description=models.TextField(max_length=1000)
	image= models.ImageField(upload_to = 'images/')	
	address=models.CharField(max_length=50, choices=(
		(u'Ghana Hola', u'Mikindani-Gahana Hola'),
		(u'Kwashee', u'Mikindani- Kwashee'),
		(u'Kwa Mwanzia', u'Mikindani- Kwa Mwanzia'),
		(u'Staff', u'Mikindani- Staff'),
		(u'Alidina', u'Mikindani- Alidina'), ))
	# full_name=models.CharField(max_length=100, null=True)
	# phone_number = PhoneNumberField(null=True)
	# email=models.EmailField(null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	date=models.DateTimeField()

	def __str__(self):
		return self.title
	
'''
	def view_user(request):
		user_profile = request.user.get_profile()
		return user_profile
'''	

	