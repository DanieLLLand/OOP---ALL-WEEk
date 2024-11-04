print("OE 3")

class SocialMediaAccount:
    def __init__(self, username, followers):
        self.username = username
        self.followers = followers
    def share_story(self):
        return f"{self.username} shared a story."

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, followers, bio):
        super().__init__(username, followers)
        self.bio = bio

class TwitterAccount(SocialMediaAccount):
    def tweet(self, message):
        return f"{self.username} tweeted: '{message}'"

insta = InstagramAccount("insta_user", 5000, "Love photos!")
twitter = TwitterAccount("twitter_user", 3000)

print(insta.share_story())
print(twitter.tweet("Hello, Twitter!"))