import instaloader
from instaloader import Profile,Post
instance = instaloader.Instaloader()
username = input("Enter your Username :")
password = input("Enter your Password :")
targetUserName = input("Enter Target Username :")
instance.login(str(username),str(password))
instance.download_profile(targetUserName)