class Tweet:

    def __init__(self):
        self.posts = {} 
        self.follows = {}
        self.last_tweets = []
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.last_tweets.insert(0, [userId, tweetId])
    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        for user, tweet in self.last_tweets:
            if user == userId or user in self.follows.get(userId , []):
                ans.append(tweet)
            if len(ans) == 10:
                break
        return ans
    def follow(self, followerId: int, followeeId: int) -> None:
        if self.follows.get(followerId) is None:
            self.follows[followerId] = [followeeId]
        else:
            self.follows[followerId].append(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows.get(followerId , []):
            self.follows[followerId].remove(followeeId)

