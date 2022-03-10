# -*- coding: utf-8 -*-
"""
HW1 Code Skeleton
@author: Jianhua Ruan
"""
import random

import matplotlib.pyplot as plt
from IPython import get_ipython


#%% Q1 Selection Sort; although not required, it should be in-place sorting (sort the original list)

def selectionSort(numList):
    """Given a list of numbers, return a list in sorted order (least to largest)
        Note that the function may change the original list (in-place sorting)
    """
    #numList = [4,8,2,1,6,9,10]
##########################
# replace this block
    for j in range(len(numList)):
        minVal = j;
        for k in range(j+1, len(numList)):
            if numList[minVal] > numList[k]:
                minVal = k
        numList[j], numList[minVal] = numList[minVal], numList[j]
    
                
        
    #pass       #commented this since no longer needed JP 
##########################

    return numList #uncommented this JP


#%% Testing selection sort

a = [random.randint(0, 20) for _ in range(10)]
print('\n\n********* Q1 *********')
print('random array is: ', a)
    
b = selectionSort(a)
print('selection sorted array is: ', b)

if b == sorted(a):
    print('selectionSort is correct') 

    print('profiling running time of python sorted function on a:')
    get_ipython().run_line_magic('timeit', 'sorted(a)')

    print('profiling running time of my merge sort function on a:')
    get_ipython().run_line_magic('timeit', 'selectionSort(a)')

else:
# replace the following statement with a print statement if your selection sort is incorrect 
# but you want to continue with the rest of the code
    raise SystemExit('selectionSort is incorrect')


#%% Q2a. Merge function

def merge(sortListA, sortListB):
    """Given two non-decreasingly sorted list of numbers, 
       return a single merged list in non-decreasing order
    """
##########################
# replace this block
    mergedList = sortListA + sortListB
    mergedList.sort() #is this how the prof wants it since we cant use numpy or panda?
   # for j in range(len(sortA), len(sortB)): #could I use zip or turn it into a tuple?
   # pass commented out since its not longer needed JP    
##########################
    return mergedList


#%% Testing merge function

a = sorted([random.randint(0, 10) for _ in range(5)]) # a is sorted 
b = sorted([random.randint(0, 10) for _ in range(4)]) # b is sorted

print('\n\n********* Q2a *********')
print('a is: ', a)
print('b is: ', b)

c = merge(a, b) # c should be sorted(a+b)
print('merged result: ', c)

if (c == sorted(a + b)):
    print('merge is correct')
else:
# replace the following statement with a print statement if your merge function is incorrect 
# but you want to continue with the rest of the code
    raise SystemExit('merge is incorrect')    


#%% Q2b merge sort; not an in-place sorting (returns a new sorted list)

def mergeSort(numList):
    """
    Given a list of numbers in random order, 
    return a new list sorted in non-decreasing order, 
    and leave the original list unchanged.
    """
##########################
# replace this block
    sortedList = numList #super slow? and it seems correct? is it?
    sortedList.sort()
    #pass commented out JP    
##########################

    return sortedList


#%% Test mergeSort function
    
    
a = [random.randint(0, 20) for _ in range(10)]
    

print('\n\n********* Q2b *********')
print('random array is: ', a)


b = mergeSort(a)
print('merge sorted array is: ', b)


if b == sorted(a):
    print('mergeSort is correct') 
    print('profiling running time of python sorted function on a:')
    get_ipython().run_line_magic('timeit', 'sorted(a)')

    print('profiling running time of my merge sort function on a:')
    get_ipython().run_line_magic('timeit', 'mergeSort(a)')

else:
# replace the following statement with a print statement if your merge sort is incorrect 
# but you want to continue with the rest of the code
    raise SystemExit('mergeSort is incorrect')




#%% Q3 run the three sorting algorithms on different input sizes and collect running time

import time

# input size is 500 * (1, 2, 4, ..., 32)
sizes = [500 * 2**i for i in range(6)]


merge_sort_time = [0] * len(sizes)
selection_sort_time = [0] * len(sizes)
quick_sort_time = [0] * len(sizes)

print('\n\n********* Q3 *********')
print('Collecting running time (in milliseconds)')

for i in range(len(sizes)):
    print('iteration %d, size = %d' %(i, sizes[i]))
    # random array of size sizes[i]
    a = [random.random() for _ in range(sizes[i])]
    start_time = time.perf_counter()
    sorted(a)
    quick_sort_time[i] = 1000*(time.perf_counter() - start_time) 
    start_time = time.perf_counter()
    mergeSort(a)
    merge_sort_time[i] = 1000*(time.perf_counter() - start_time) 
    start_time = time.perf_counter()
    selectionSort(a)
    selection_sort_time[i] = 1000*(time.perf_counter() - start_time)  




# complete the following code to plot the running time; use the style show in the homework 
# document as template, reproduce as much detail as possible.

#%% Q3a. plot running time (Fig 1)

##########################
# replace this block
    plt.figure() #figure out plt.plot for a, start time might be wrong, markers might be x or *
    plt.plot(sizes, merge_sort_time, color='green', marker='*',linestyle='solid')
    plt.plot(sizes,selection_sort_time, color='blue', marker='x',linestyle='-.')
    plt.plot(sizes,quick_sort_time, color='orange', marker='x',linestyle=':')
    plt.title('Fig 1')
   # plt.xlim(,16000)
   # plt.ylim(,10000)
    plt.ylabel('Time (ms)')
    plt.xlabel("Input Size")
    plt.show()
    #pass    
##########################

    

#%% Q3b. plot running time (Fig 2)

##########################
# replace this block
    plt.figure() #figure out plt.plot for a, start time might be wrong, markers might be x or *
    plt.plot(sizes, merge_sort_time, color='green', marker='*',linestyle='solid')
    plt.plot(sizes,selection_sort_time, color='blue', marker='x',linestyle='-.')
    plt.plot(sizes,quick_sort_time, color='orange', marker='x',linestyle=':')
    plt.title('Fig 2')
 #   plt.xlim(,16000)
   # plt.ylim(,10000)
    plt.ylabel('Time (ms)')
    plt.xlabel("Input Size")
    plt.show()
    #pass    
##########################



#%% Q3c. plot running time per input element (Fig 3)

##########################
# replace this block
    plt.figure() #figure out plt.plot for a, start time might be wrong, markers might be x or *
    plt.plot(sizes, merge_sort_time, color='green', marker='*',linestyle='solid')
    plt.plot(sizes,selection_sort_time, color='blue', marker='x',linestyle='-.')
    plt.plot(sizes,quick_sort_time, color='orange', marker='x',linestyle=':')
    plt.title('Fig 3')
    #plt.xlim(,16000)
    #plt.ylim(,10000)
    plt.ylabel('Time (ms)')
    plt.xlabel("Input Size")
    plt.show()    
#pass    
##########################


#%% Q3d. plot running time per input element (Fig 4)

##########################
# replace this block
    #pass
    plt.figure() #figure out plt.plot for a, start time might be wrong, markers might be x or *
    plt.plot(sizes, merge_sort_time, color='green', marker='*',linestyle='solid')
    plt.plot(sizes,selection_sort_time, color='blue', marker='x',linestyle='-.')
    plt.plot(sizes,quick_sort_time, color='orange', marker='x',linestyle=':')
    plt.title('Fig 4')
   # plt.xlim(,16000)
   # plt.ylim(,10000)
    plt.ylabel('Time (ms)')
    plt.xlabel("Input Size")
    plt.show()    
##########################
