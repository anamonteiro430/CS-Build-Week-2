https://leetcode.com/problems/contains-duplicate/

''' Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false '''

#Create dict for easy lookup and insert
#iterate through list given
#add the count to dict
#iterate through dict and if any value is over 1 return True since there's duplicates

class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1      
        
        for key in dict:
            if dict[key] > 1:
                return True
        return False