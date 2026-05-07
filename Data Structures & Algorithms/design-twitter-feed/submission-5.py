class Twitter:

    def __init__(self):
        self.tweets = []
        self.followers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))
        self.followers.setdefault(userId, set())

    def getNewsFeed(self, userId: int) -> List[int]:
        i = len(self.tweets) - 1
        res = []
        while i >= 0 and len(res) < 10:
            uId, tId = self.tweets[i]
            if uId in self.followers[userId] or userId == uId:
                res.append(tId)
            i -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers.setdefault(followerId, set())
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers.setdefault(followerId, set())
        self.followers[followerId].discard(followeeId)

