"""
User Manager.py
"""
#models
from django.contrib.auth.models import User


class UserManager():

	def addUser(self,username, password, email):
		user = User.objects.create_user(username=username, password = password)