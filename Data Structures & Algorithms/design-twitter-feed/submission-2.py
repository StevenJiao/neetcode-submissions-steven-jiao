class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = deque()
        self.userToUsers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # heapq.heappush_max(self.tweets, [self.time, tweetId, userId])
        self.tweets.appendleft([tweetId, userId])
        # self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        userFollowing = self.userToUsers.get(userId, set([str(userId)]))
        userFeed = [tweet[0] for tweet in self.tweets if str(tweet[1]) in userFollowing]
        return userFeed[0:10]
        # self.time += 1

    def follow(self, followerId: int, followeeId: int) -> None:
        followers = self.userToUsers.get(followerId, set([str(followerId)]))
        followers.add(str(followeeId))
        self.userToUsers[followerId] = followers
        # self.time += 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followers = self.userToUsers.get(followerId, set([str(followerId)]))
        followers.remove(str(followeeId)) if str(followeeId) in followers and followerId != followeeId else None
        self.userToUsers[followerId] = followers
        # self.time += 1
