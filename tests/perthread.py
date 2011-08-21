import yappi
import time
import threading

class MyThread(threading.Thread):
    def run(self):
        time.sleep(1)
	# do a cpu-intensive work
	i = 0
	while(i < 1000000):
	    i += 1

n = 1

yappi.start()

for i in range(0,n):
    c = MyThread()
    c.start()
yappi.stop()
yappi.print_stats()
