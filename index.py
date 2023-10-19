import instaloader

ig=instaloader.Instaloader()#create an instaload object

username=input("enter username:")

profile=instaloader.Profile.from_username(ig.context,username)

print("username:",profile.username)
print("no of posts:",profile.mediacount)
print("bio:",profile.biography)
print(profile.username + "has followers:" + str(profile.followers))
print(profile.username + "is following:" + str(profile.followees))

instaloader.Instaloader().download_profile(username,profile_pic_only=True)
