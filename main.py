nric = input('Enter an NRIC number: ')

# Type your code below

check = 'invalid'
sum = 0
count = 0
weight = [2,7,6,5,4,3,2]
Grp1 = ["J","Z","I","H","G","F","E","D","C","B","A"]
Grp2 = ["X","W","U","T","R","Q","P","N","M","L","K"]
nric = nric.upper()
letter = ["S","T","F","G"]
if len(nric) == 9:
  if nric[0] in letter:
    a = nric[0]
    if (nric[8]).isalpha:
      b = nric[8]
      new = nric[1:8]
      for x in new:
        sum += (int(x)*weight[count])
        count += 1
      if a == "T" or a == "G":
        sum += 4
      r = (sum % 11) 
      if a == "T" or a == "S":
        digit = Grp1[r]
      else:
        digit = Grp2[r]
      if b == digit:
        check = "valid"

print("NRIC is {}.".format(check))