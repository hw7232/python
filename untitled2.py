# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:42:09 2021

@author: user
"""

List = ['F', 'B','C','A','E','D']

List = List[::-1]
print(List)
List = List[1:-1]
print(List)
List = List[-2::-1]
print(List)
List.sort(reverse = True)
print(List)
List.append('G')
print(List)
List.sort(reverse = False)
print(List)