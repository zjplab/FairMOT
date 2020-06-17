from heapq import *

'''
Need to specify key function for custom data structures for comaprision in a min heap 

'''
class _Wrapper:
    def __init__(self, item, key):
        self.item = item
        self.key = key

    def __lt__(self, other):
        return self.key(self.item) < other.key(other.item)

    def __eq__(self, other):
        return self.key(self.item) == other.key(other.item)

    def __repr__(self):
        return str(self.item)

class KeyPriorityQueue:
    '''
    Custom Priority Queue with maximum length and custom type support
    '''
    def __init__(self, key, maxLen):
        self.key = key
        self.queue=[]
        self.maxLen=maxLen

    def _get(self):
        wrapper = heappop(self.queue)
        return wrapper.item
    
    def get(self):
        return self._get()
    
    def peek(self):
        return self.queue[0]

    def _put(self, item):
        heappush(self.queue, _Wrapper(item, self.key))

    def put(self, item):
        if(self._qsize() == self.maxLen):
            heappop(self.queue)
        self._put(item)

    def _qsize(self):
        return len(self.queue)

    def nlargest(self, n):
        return nlargest(n, self.queue, key=lambda x: self.key(x.item))
    
    def nsmallest(self, n):
        return nsmallest(n, self.queue, key=lambda x: self.key(x.item))


# testing scirpt
if __name__=='__main__':
    data=[(3, 3.5556), (-2, -3), (100, 2)]
    key= lambda x:x[1]
    q=KeyPriorityQueue(key, 2)
    for item in data:
        q.put(item)
    print(q.nlargest(2))
    print(q.nsmallest(2))