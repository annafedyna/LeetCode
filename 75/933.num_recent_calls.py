class RecentCounter:
    
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue and self.queue[0] < t-3000:
            self.queue.pop(0)
        return len(self.queue)


obj = RecentCounter()
param_1 = obj.ping(1)
param_2 = obj.ping(2)

'''
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). 
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
'''