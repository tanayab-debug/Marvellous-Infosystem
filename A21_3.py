import threading

icnt = 0
lobj = threading.Lock()

def update():
    global icnt
    for _ in range(500):
        with lobj:
            icnt = icnt + 1

def main():
    global icnt
    t1 = threading.Thread(target=update)
    t2 = threading.Thread(target=update)
    t3 = threading.Thread(target=update)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t1.join()
    t3.join()

    print("icnt: ", icnt)

if __name__ == "__main__":
    main()