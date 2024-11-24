from threading import Thread, Event, currentThread
import time

# UserInofmations
# name age
# amir 20

# Games Detial
# name , score , user
# Rainbow,100,1


def f(e: Event):
    print("salam bache ha chetorid ")
    e.wait()
    print("khodahafez ey doost khoobam ")


def g(e: Event):
    time.sleep(3)
    print("be yad nami oo ke hast ")
    e.set()


e = Event()

t = Thread(name='t', target=f, args=(e,))
s = Thread(name='s', target=g, args=(e,))


t.start()
s.start()
