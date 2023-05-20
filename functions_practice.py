def hello():
    print("Hello!")

def pack(a, b, c):
    return [a, b, c]



#def eat_lunch(list):
#    for i in list:
#        if list[i] == 0:
#            print(f"First I eat {[i]}")
#        elif len(list) == 0:
#            print("My lunchbox is empty.")
#       else:
#            print(f"Next I eat {[i]}")

def eat_lunch(list):
  if len(list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(list)):
      if i == 0:
        print(f"First I eat {list[0]}")
      else:
        print(f"Next I eat {list[i]}")


hello()
print(pack("book", "pencils", "calculator"))
eat_lunch(["pasta"])
eat_lunch([])
eat_lunch(["cheese", "cracker", "milk"])

# ["cheese", "cracker", "milk"]