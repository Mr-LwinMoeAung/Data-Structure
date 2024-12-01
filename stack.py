#push = add the elements to the stack (append)
#pop = remove the elements from the stack (pop)
#peek or top = element present at the top [-1]
#isEmpty = check the stack is empty or not (len) (not list_name)

#stack: using lists and modules
#paper stack (first-last , last-serve)
#push need elements, others don't


# stack=[]

# def push():
#     inp=input('Enter to push : ')
#     if len(stack)==5:
#         print('Stack is full')
#     else:
#         stack.append(inp)
#         print(stack)

# def pop():
#     if not stack:
#         print('Stack is empty')
#     else:
#         stack.pop()
#         print('Removed element : ',stack.pop())
#         print(stack)

# def peek():
#     print(stack[-1])

# def isEmpty():
#     if not stack:
#         print('Stack is full')
#     else:
#         print('It is not full yet',len(stack))


# print('Stack limit = 5')

# while True:
#     user=int(input('Enter : 1-push , 2-pop , 3-peek , 4-check , 5-stop: '))
#     if user==1:
#         push()
#     if user==2:
#         pop()
#     if user==3:
#         peek()
#     if user==4:
#         isEmpty()
#     if user==5:
#         print('End')
#         break


#Collections - deque -> double ended queue
# import collections
# stack=collections.deque()
# just append and pop





#import queue
#Queue - LifoQueue() queue 
# push - put() method
# pop - get() method
#LifoQueue(3) -> 3 is the stack limit
#Nothing will print after 3, to print pust(,timeout)