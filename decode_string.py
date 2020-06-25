#k[encoded_string]
#iterate over string
#if i is equal to "[" i-1 is the number and until it reaches "]" that's a part of the string
#put those values in variables
#after looping to the math

class Solution:
         def decodeString(self, s: str) -> str:
        
          print("this is string", s)
          for i in s:
               if i == "[":
                    
                    number = i-1
                    value = i+1