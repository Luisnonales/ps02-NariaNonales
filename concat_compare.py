import time

start = time.time()
result = ""
for i in range (1, 100001):
    result += str(i)
print("+= Time: ", time.time() - start)

start = time.time()
result = "".join(str(i)for i in range(1, 100001))
print ("Using join(): ", time.time() - start)
