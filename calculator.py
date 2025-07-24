# what user wants to calc
print("Please enter ~ instead of - if you want to subtract.")
x = input("What do you want to calculate: ")

vlist = []

# finding the numbers
newstr = ''.join((ch if ch in '0123456789.e-' else ' ') for ch in x)
xlist = [float(i) for i in newstr.split()]

# finding the operations
newstr2 = ''.join((ch if ch in '+~x*/^' else ' ') for ch in x)
signlist = [i for i in newstr2.split()]

# variables and stuff
xlen = len(xlist)
slen = len(signlist)

minlen = min(xlen, slen)

answer = 0

j = 0

exception = False
noanswer = False

# combining lists
for i in range(0,minlen):
  vlist.append(xlist[i])
  vlist.append(signlist[i])

vlist += xlist[minlen:] + signlist[minlen:]
#print(vlist)

# variables 2
vlen = len(vlist)

# math
if vlen > 1:
  while j < vlen:
    #print("counter:", j)
    #print("vlen:", vlen)
    if vlist[j] ==  "^":
      #print("Before replacement", vlist)
      vlist[j] = "pl"
      #print("After replacement", vlist)
      if "^" in vlist:
        j += 1
        continue
      else:
        vlist = ["^" if x == "pl" else x for x in vlist]
        #print("Fixed list", vlist)
      try:
        raw = float(vlist[j-1]) ** float(vlist[j+1])
        vlist[j] = raw
        #print("Before deletion", vlist)
        del vlist[j+1]
        del vlist[j-1]
        #print("After deletion", vlist)
        j = 0
        vlen = len(vlist)
      except OverflowError:
          print("The calculation was too big!")
          exception = True
          break
    elif vlist[j] ==  "x" or vlist[j] == '*':
      if "^" in vlist:
        j += 1
        continue
      else:
        raw = float(vlist[j-1]) * float(vlist[j+1])
        vlist[j] = raw
        #print("Before deletion", vlist)
        del vlist[j+1]
        del vlist[j-1]
        #print("After deletion", vlist)
        j = 0
        vlen = len(vlist)
    elif vlist[j] ==  "/":
      if "^" in vlist:
        j += 1
        continue
      else:
        raw = float(vlist[j-1]) / float(vlist[j+1])
        vlist[j] = raw
        #print("Before deletion", vlist)
        del vlist[j+1]
        del vlist[j-1]
        #print("After deletion", vlist)
        j = 0
        vlen = len(vlist)
    elif vlist[j] ==  "+":
      if "^" in vlist:
        j += 1
        continue
      elif "*" in vlist or "/" in vlist or "x" in vlist:
        j += 1
        continue
      else:
        raw = float(vlist[j-1]) + float(vlist[j+1])
        vlist[j] = raw
        #print("Before deletion", vlist)
        del vlist[j+1]
        del vlist[j-1]
        #print("After deletion", vlist)
        j = 0
        vlen = len(vlist)
    elif vlist[j] ==  "~":
      if "^" in vlist:
        j += 1
        continue
      elif "*" in vlist or "/" in vlist or "x" in vlist:
        j += 1
        continue
      else:
        raw = float(vlist[j-1]) - float(vlist[j+1])
        vlist[j] = raw
        #print("Before deletion", vlist)
        del vlist[j+1]
        del vlist[j-1]
        #print("After deletion", vlist)
        j = 0
        vlen = len(vlist)
    j += 1

answer = vlist[0]

# Printing Answer
if exception == False and noanswer == False:
  print("Your answer is:", answer)