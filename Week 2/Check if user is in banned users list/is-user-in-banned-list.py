# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:22:01 2017

@author: Dimitar Nikolov
"""

# Set banned user names
banned_users = ['andrew', 'carolina', 'david']

# Set current user name
logged_in_user = 'marie'

# Print message to the user that permits him/her to post a comment.
if logged_in_user not in banned_users:
    print(logged_in_user.title() + ", you can post a comment.")