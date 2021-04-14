# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

def get_input_data():
    try:
        return input()
    except Exception as e:
        print(f'Error: {e}')
        exit(1)


if __name__ == "__main__":
    
   s = get_input_data() 
   k = get_input_data()
   
   #Constraints validation
   if len(s) < 0 or len(s) > 100:
      print('Constraints One')
      exit(1)
   elif len(k) < 0 or len(k) > len(s):
      print('Constraints Two')
      exit(1)
   
   result = map(lambda m: (m[1].start(0) + m[0], m[1].end(0) + m[0] -1),  [(i , re.search(f'({k})', s[i:])) for i in range(len(s)) if re.search(f'({k})', s[i:])])
   #Constraints validation
   if len(s) < 0 or len(s) > 100:
      print('Constraints One')
      exit(1)
   elif len(k) < 0 or len(k) > len(s):
      print('Constraints Two')
      exit(1)
   
   #Print result
   result = map(lambda m: (m[1].start(0) + m[0], m[1].end(0) + m[0] -1),  [(i , re.search(f'({k})', s[i:])) for i in range(len(s)) if re.search(f'({k})', s[i:])])
   if result:
      l_result = sorted(list(set(list(result))), key=lambda x: x)
      for r in l_result:
        print(r)
   else:
      print((-1,-1))


'''

Ref: 
   - https://levelup.gitconnected.com/sort-elements-in-python-817a0c2b810b
   - https://thispointer.com/python-how-to-use-if-else-elif-in-lambda-functions/

'''