"""
LeetCode 1200 - Minimum Absolute Difference
Difficulty: Easy
Topic: Arrays
"""

class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        minimum=float('inf')
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<minimum:
                minimum=arr[i+1]-arr[i]
        result=[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==minimum:
                result.append([arr[i],arr[i+1]])
        return result
                
