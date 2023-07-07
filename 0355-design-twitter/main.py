import time

class Twitter:

    def __init__(self):
        self.tweets = {}  # Foydalanuvchi tweetlarini saqlash uchun lug'at
        self.followees = {}  # Foydalanuvchilar tomonidan kuzatiladigan odamlarni saqlash uchun lug'at
        self.time = 0  # Vaqt belgilari

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Foydalanuvchi tweetlarini qo'shish uchun
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Foydalanuvchining o'zining va kuzatuvchi foydalanuvchilarining tweetlarini qaytarish uchun
        tweets = []
        if userId in self.tweets:
            tweets.extend(self.tweets[userId])
        if userId in self.followees:
            for followeeId in self.followees[userId]:
                if followeeId in self.tweets:
                    tweets.extend(self.tweets[followeeId])
        # Vaqt belgilari bo'yicha oxirgi 10 ta tweetni qaytarish uchun
        tweets.sort(key=lambda x: x[1], reverse=True)
        return [tweet[0] for tweet in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        # Foydalanuvchi boshqa foydalanuvchini kuzatish uchun
        if followerId not in self.followees:
            self.followees[followerId] = set()
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Foydalanuvchi kuzatuvchi foydalanuvchini kuzatishdan chiqarish uchun
        if followerId in self.followees and followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


# Namuna ishlatish

twitter = Twitter()

# Foydalanuvchilar
twitter.postTweet(1, 5)  # Foydalanuvchi 1, tweet 5 ni joyladi
print(twitter.getNewsFeed(1))  # Foydalanuvchi 1 ning tweetlarini ko'rish (faqat o'zining tweetlari)

twitter.follow(1, 2)  # Foydalanuvchi 1, foydalanuvchi 2 ni kuzatishni boshladi
twitter.postTweet(2, 6)  # Foydalanuvchi 2, tweet 6 ni joyladi
print(twitter.getNewsFeed(1))  # Foydalanuvchi 1 ning tweetlarini ko'rish (o'zining tweetlari + kuzatgan foydalanuvchi tweeti)

twitter.unfollow(1, 2)  # Foydalanuvchi 1, foydalanuvchi 2 ni kuzatishdan chiqdi
print(twitter.getNewsFeed(1))  # Foydalanuvchi 1 ning tweetlarini ko'rish (faqat o'zining tweetlari)
