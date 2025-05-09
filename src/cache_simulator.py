import threading
import time

shared_memory = {'x': 0}
lock = threading.Lock()

class Cache:
    def __init__(self, name):
        self.name = name
        self.local_copy = {}

    def read(self, var):
        return self.local_copy.get(var, None)

    def write(self, var, value):
        self.local_copy[var] = value

def thread_job(cache, coherence=False):
    for i in range(3):
        with lock:
            val = shared_memory['x']
            print(f"[{cache.name}] READ shared x = {val}")

        if coherence:
            cache.write('x', val)  # simpan ke cache lokal

        new_val = val + 1
        time.sleep(0.1)

        with lock:
            shared_memory['x'] = new_val
            print(f"[{cache.name}] WRITE shared x = {new_val}")

def simulate(use_coherence=False):
    cache1 = Cache("CPU1")
    cache2 = Cache("CPU2")

    t1 = threading.Thread(target=thread_job, args=(cache1, use_coherence))
    t2 = threading.Thread(target=thread_job, args=(cache2, use_coherence))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Final shared memory:", shared_memory)

if __name__ == "__main__":
    print("=== SIMULASI TANPA KOHERENSI ===")
    shared_memory['x'] = 0
    simulate(use_coherence=False)

    print("\n=== SIMULASI DENGAN KOHERENSI ===")
    shared_memory['x'] = 0
    simulate(use_coherence=True)
