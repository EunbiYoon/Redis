import redis
import time 

#connect
r=redis.Redis()

r.set("foo","bar")
print(r.get("foo"))
r.expire("foo",20) #foo key will expire after 20 seconds
time.sleep(20)
print(r.get("foo"))
print(r.ttl("foo"))
