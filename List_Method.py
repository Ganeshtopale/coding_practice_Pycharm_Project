print("......list method......")
list  = [2,4,6,8,10,12,4,16,18,20]
list.sort()
print(list)

list.reverse()
print(list)

list.append(22)
print(list)

list.insert(5,25)
print(list)

list.remove(10)
print(list)

list.insert(6,100)
print(list)


print(".......dictionary methhods...................")

d = {1:"john",2:"ram",3:"rohan"}
print(d.values())
print(d.keys())

dictionary = {"apples":3,"bananas":4,"pears":5,"lemons":10}
a = ["apples","lemons"]
b = {key:dictionary[key] for key in a}
print(b)

def foo (i):
  return (((i*2)-3)%3)

x = foo(6)
print(x)


s = {'e':4,'f':5}
s[1]
print(s)

