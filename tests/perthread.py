import yappi
import time
import threading

class MyThread(threading.Thread):
    def run(self):
        time.sleep(1)
        # do a cpu-intensive work
        i = 0
        j = 3
        while(i < 100000):
            i += 1
            j *= i

def foo():
    #n = 1
    #for i in range(0,n):
    c = MyThread()
    c.start()
    c.join()



#yappi.start(builtins=True)
yappi.start()
foo()
yappi.stop()
yappi.print_stats()
