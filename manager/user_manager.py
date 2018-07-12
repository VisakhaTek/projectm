"""
User Manager.py
"""
#models
from django.contrib.auth.models import User


class UserManager():

	def addUser(self,username, password, email):
		user = User()
		user.username = username
		user.email = email
		user.password = password
		user.save()