from time import ctime,sleep

def loop0():
    print("starting loop 0 at:", ctime())
    sleep(4)
    print("loop 0 done at:", ctime())

def loop1():
    print("starting loop 1 at:", ctime())
    sleep(2)
    print("loop 1 done at:", ctime())

def main():
    print("the process is running at:", ctime())
    loop0()
    loop1()
    print("all Done at:", ctime())

if __name__ == '__main__':
    main()