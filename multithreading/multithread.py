import threading
import os

# to calculate the square and cube of a number concurrently.

def cube(x):
    print("id of the current thread is ", os.getpid())
    print("name of current thread", threading.current_thread().name)
    
    print("cube is ", x * x* x)

def square(x):
    print("id of the current thread is ", os.getpid())
    print("name of current thread", threading.current_thread().name)
    
    print("square is", x *x)


if __name__ == "__main__":

    print("id of the current thread is ", os.getpid())
    print("name of current thread", threading.current_thread().name)
    x = threading.Thread(target=cube, args=(10,), name = "cube")
    y = threading.Thread(target=square, args=(10,), name = "square")

    x.start()
    y.start()

    x.join()
    y.join()

    print("done")