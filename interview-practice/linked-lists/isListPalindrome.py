"""Note: Try to solve this task in O(n) time using O(1) additional space, where
n is the number of elements in l, since this is what you'll be asked to do during
an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

asked by- Amazon & Facebook"""



# def isListPalindrome(l):
#     a = []
#     while l != None:
#         a.append(l.value)
#         l = l.next
#     return a == a[::-1]


# def isListPalindrome(l):
#     size = 0
#     cur = l
#     while cur:
#         size += 1
#         cur = cur.next
#     if size == 1:
#         return True
#     flag = 0
#     if size % 2 != 0:
#         flag = 1
#     cur = l
#     stack = []
#     c = 0
#     size = size // 2
#     while cur:
#         c += 1
#         if c <= size:
#             stack.append(cur.value)
#         else:
#             if flag == 1:
#                 cur = cur.next
#                 flag = 0
#             else:
#                 if cur.value != stack[-1]:
#                     return False
#             stack.pop()
#         cur = cur.next
#     return True

def isListPalindrome(l):
    if l == None:
        return True
    # set i to point to middle of list using runner j
    i = j = l
    while j.next != None:
        j = j.next.next
        if j == None:
            break
        i = i.next
    # reverse second half of list 
    h = i.next
    k = None
    while h != None:
        j = h.next
        h.next = k
        k = h
        i.next = h
        h = j
    # match first half to reversed second half
    i = i.next
    while i != None:        
        if l.value != i.value:
  		    return False      
        i = i.next
        l = l.next
    return True