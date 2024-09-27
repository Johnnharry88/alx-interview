#!/usr/bin/python3
"""Module for solving  primegame"""

def isWinner(x, nums):
     """Function to check fr the winner """
     if not nums or x < 1:
          return None
     max_no = (max(nums))
     selector = [True for y in range(max(max_no + 1, 2))]
     for i in range(2, int(pow(max_no, 0.5)) + 1):
          if not selector[i]:
               continue
          for j in range(i * i, max_no + 1, i):
               selector[j] =  False
     selector[0] = selector[1] = False
     a = 0
     for i in range(len(selector)):
          if selector[i]:
               a = a + 1;
          selector[i] = a
     gamer = 0
     for x in nums:
          gamer = gamer + selector[x] % 2 == 1
     if gamer * 2 > len(nums):
          return "Maria"
     return "Ben"
