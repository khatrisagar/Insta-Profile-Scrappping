import instaloader

client = instaloader.Instaloader()

profile = instaloader.Profile.from_username(client.context,'khatrisagar99')

print("Username:", profile.username)
print("User ID:", profile.userid)
print("Number of Posts: ",profile.mediacount)
print("Followers: ", profile.followers)
print("Followings: ", profile.followees)
print("Bio: ", profile.biography)
print("Link In Bio: ", profile.external_url)
