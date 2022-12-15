import dddd
import time

#connect
r=dddd.Redis(host='127.0.0.1', port=6379)

# set single data
r.set("France","Paris")
r.set("Germany","Berlin")
france_capital=r.get("France")
germany_capital=r.get("Germany")
print("set single data")
print(france_capital)
print(germany_capital)

# set multiple data
r.mset({"Germany":"Berlin","France":"Paris"})
print("set multiple data")
print(r.get("France"))
print(r.get("Germany"))

#if condition 
if (r.exists("Germany")):
    print("Data Exist")
    print(r.get("Germany"))
else:
    print("Cannot fnid the capital. Getting from API")

#psetex
print("psetex")
r.psetex("Germany",1000, "Berlin") #ttl 1000ms=1s, set Germany Key to Berlin Value
print(r.get("Germany")) #check data input
time.sleep(2) #time pass 2 second
print(r.get("Germany")) #check data remained