from python.stacksAndQueues.stack_and_queues import Queue


class AnimalShelter:

    def __init__(self):
        self.catQueue = Queue()
        self.dogQueue = Queue()

    def enqueue(self,animal):
        if "dog" in animal:
            self.dogQueue.enqueue(animal)
        elif "cat" in animal:
            self.catQueue.enqueue(animal)
        else:
            raise ValueError('Error')
    
    def dequeue(self,pref):
        if pref == "dog":
            self.dogQueue.dequeue()
            return "dog"
        elif pref == "cat":
            self.catQueue.dequeue()
            return "cat"
        else:
            return "Null"