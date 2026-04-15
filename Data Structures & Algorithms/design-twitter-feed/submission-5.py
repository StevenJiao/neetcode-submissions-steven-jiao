class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {} # (time, tweetId)
        self.userToUsers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        userTweets = self.tweets.get(userId, [])
        userTweets.append((self.time, tweetId))
        self.tweets[userId] = userTweets
        if (len(self.tweets[userId]) > 10):
            self.tweets[userId].pop(0)
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followees = self.userToUsers.get(userId, set([userId]))
        for follow in followees:
            tweets = self.tweets.get(follow, [])
            for tweet in tweets:
                tweetTime, tweetId = tweet
                if len(heap) == 10 and tweetTime < heap[0][0]:
                    heapq.heappop_max(heap)
                    heapq.heappush_max(heap, tweet)
                elif len(heap) < 10:
                    heapq.heappush_max(heap, tweet)
        sortedTweets = sorted(heap,key=lambda x: x[0])
        return [t[1] for t in sortedTweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        followees = self.userToUsers.get(followerId, set([followerId]))
        followees.add(followeeId)
        self.userToUsers[followerId] = followees

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userToUsers.get(followerId, set([followerId])):
            followees = self.userToUsers[followerId]
            followees.remove(followeeId) if followerId != followeeId else None
            self.userToUsers[followerId] = followees
