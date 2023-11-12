class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.capacity - self.front + self.rear + 1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
        else:
            removed_item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity
            return removed_item

cq = CircularQueue(5)

print("Is the queue empty?", cq.is_empty())  
print("Is the queue full?", cq.is_full())    
print("Queue size:", cq.size())               

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

print("Is the queue empty?", cq.is_empty())  
print("Is the queue full?", cq.is_full())    
print("Queue size:", cq.size())               

cq.enqueue(40)
cq.enqueue(50)

print("Is the queue full?", cq.is_full())    

print("Dequeue:", cq.dequeue())               
print("Queue size:", cq.size())              
