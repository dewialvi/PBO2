from threading import Thread

class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        
    def run(self):
        print("Thread {} is running".format(self.name))

t1 = MyThread("1")
t2 = MyThread("2")

t1.start()
t2.start()

t1.join()
t2.join()
