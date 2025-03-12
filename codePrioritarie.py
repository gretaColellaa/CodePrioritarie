import datetime
import queue
import random


class CodaPrioritaria:
    def __init__(self):
        self._lista = []

    def put(self, x):
        """
        Aggiungo un nuovo elemento alla coda
        :param x:
        :return:
        """
        self._lista.append(x)

    def get(self):
        """
        Restituisce l'elemento più piccolo presente
        nella coda, e lo elimina
        :return:
        """
        index, val = min(enumerate(self._lista), key=lambda x: x[1])
        self._lista.pop(index)
        return val[1]

    def __len__(self):
        return len(self._lista)


# c = CodaPrioritaria()

c = queue.PriorityQueue()

c.put((3, "ciao"))
c.put((1, "hello"))
c.put((2, "test"))

print(c.get()[1])
print(c.get()[1])
print(c.get()[1])

c1 = CodaPrioritaria()
tic = datetime.datetime.now()
for i in range(10000):
    c1.put((random.randint(0, 100), random.randint(0, 100)))

for i in range(len(c1)):
    c1.get()

toc = datetime.datetime.now()
print(f"La tua implementazione di Coda prioritaria ci ha messo {toc - tic} secondi")

c2 = queue.PriorityQueue()
tic = datetime.datetime.now()
for i in range(10000):
    c2.put((random.randint(0, 100), random.randint(0, 100)))

for i in range(c2.qsize()):
    c2.get()

toc = datetime.datetime.now()

print(f"L'implementazione di default ci mette {toc-tic} secondi")