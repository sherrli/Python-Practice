# (EXAMPLE) Distinguishing multiple exit points in loops:

# Find a target value within a sequence without using a boolean flagger
# "if" within a for loop can be combined with an "else" outside of the loop

def find(sequence, target):
   print(str(enumerate(sequence)))
   for i, value in enumerate(sequence):
       print(value)
       if value == target:
         break
   else:
      return -1
   return i

# if (if value == target) never reached in the for loop, then the "else: return -1" outside of the loop actually executes!
# sequence = ['red', 'blue', 'white']
# enumerate(sequence) makes [(0, 'red'), (1, 'blue'), (2, 'white')]

def main():
   sequence = ['r', 'b', 'w']
   print(find(sequence, 'g'))

#-----------

main()
