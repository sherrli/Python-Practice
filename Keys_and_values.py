# Looping over a key
# Should we return the key or the value?

def main():
   d = {'math': 'red', 'writing': 'green', 'science': 'blue'}
   for k in d:
      print(k)

# Keys are the entries before the colon
   for k in d.keys():
      if k.startswith('w'):
         print(d[k])
# Print the values: after the colon (prints red, green, blue)
   print (d.values())

#----- call main ---
main()
