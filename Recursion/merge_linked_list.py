"""
URL: https://leetcode.com/problems/merge-two-sorted-lists/?envType=problem-list-v2&envId=recursion
DIFF: Easy
"""

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None


list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)

list2 = Node(1)
list2.next = Node(3)
list2.next.next = Node(4)


def merge(list1,list2,l3):
    list3 = Node(-1)
    l3 = list3
    while list1 or list2:
        if not list1:
            list3.next = list2
            break

        if not list2:
            list3.next = list1
            break

        # Get the LHS and move next
        if list1.val <= list2.val:
            list3.next = Node(list1.val)
            list1 = list1.next
        elif list1.val > list2.val:
            list3.next = Node(list2.val)
            list2 = list2.next
        list3 = list3.next
    return l3.next

list3 = merge(list1,list2,None)

while list3:
    print(list3.val)
    list3 = list3.next

import sys
sys.exit()


def merge(l1,l2,l3):
    if not l1 and not l2:
        return None
    
    if not li:
        return l2

    if not l2:
        return l1

    if l1.val <= l2.val:
        return l1

    if l1.val > l2.val:
        return l2

    l3 = merge(l1,l2,l3)

