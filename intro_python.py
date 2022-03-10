


# In[ ]:
        
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]
list_length = len(integer_list) # equals 3
list_sum = sum(integer_list) # equals 6


# ## Get the i-th element of a list

# In[129]:


x = [i for i in range(10)] # is the list [0, 1, ..., 9]
zero = x[0] # equals 0, lists are 0-indexed
one = x[1] # equals 1
nine = x[-1] # equals 9, 'Pythonic' for last element
eight = x[-2] # equals 8, 'Pythonic' for next-to-last element


# ## Get a slice of a list

# In[ ]:


one_to_four = x[1:5] # [1, 2, 3, 4]
first_three = x[:3] # [0, 1, 2]
last_three = x[-3:] # [7, 8, 9]
three_to_end = x[3:] # [3, 4, ..., 9]
without_first_and_last = x[1:-1] # [1, 2, ..., 8]
copy_of_x = x[:] # [0, 1, 2, ..., 9]
another_copy_of_x = x[:3] + x[3:] # [0, 1, 2, ..., 9]


# ### More on slicing

# In[152]:


import random
random.seed(10)
x=[random.randint(0, 100) for i in range(10)]
print('x is ', x)

print('x[1::] is', x[1::])



# In[141]:


x[::3]


# In[142]:


x[-1:0:-1]




# ## Check for memberships

# In[ ]:


1 in [1, 2, 3] # True
0 in [1, 2, 3] # False


# ## Concatenate lists

# In[120]:


x = [1, 2, 3]
y = [4, 5, 6]
x.extend(y) # x is now [1,2,3,4,5,6]
print('x is', x)


# In[122]:


x = [1, 2, 3]
y = [4, 5, 6]
z=x.extend(y)
print('x is', x) # what is in x?
print('z is ', z) # what is in z? 


# In[123]:


y[0]=100 # does changing y affect x?
x


# In[125]:


x = [1, 2, 3]
y = [4, 5, 6]
z = x + y  # z is [1,2,3,4,5,6]; x is unchanged.
z


# # Dictionaries

# ## A dictionary associates values with unique keys

# In[93]:


empty_dict = {}                         # Pythonic
empty_dict2 = dict()                    # less Pythonic 
grades = { "Joel" : 80, "Tim" : 95 }    # dictionary literal 


# ## Access/modify value with key

# In[95]:


joels_grade = grades["Joel"]          # equals 80 

grades["Tim"] = 99                    # replaces the old value 
grades["Kate"] = 100                  # adds a third entry 
num_students = len(grades)            # equals 3 


# In[96]:


try:    
    kates_grade = grades["Kate"] 
    print (kates_grade)
except KeyError:    
    print("no grade for Kate!")
    
try:    
    kathy_grade = grades["Kathy"] 
    print (kathy_grade)
except KeyError:    
    print("no grade for Kathy!")


# ## Check for existence of key

# In[97]:


joel_has_grade = "Joel" in grades     # True 
kathy_has_grade = "Kathy" in grades     # False 
print(kathy_has_grade)


# ## Use “get” to avoid keyError and add default value

# In[98]:


joels_grade = grades.get("Joel", 0)   # equals 80 
kim_grade = grades.get("Kim", 0)   # equals 0 
no_ones_grade = grades.get("No One")  # default default is None 

print('Kim grade: ', kim_grade)

print('dict content: ', grades)


# ## Get all items

# In[111]:


all_keys = grades.keys()	# return a "virtual list" (iterable, but not index-accessable) of all keys
all_values = grades.values() # return a "virtual list" of all values
all_pairs = grades.items() # a "virtual list" of (key, value) tuples

for key in all_keys: 
    print (key)  # okay; all_keys is iterable
    
key0 = list(all_keys)[0]  # okay; convert to list
print ('key 0 is: ', key0)
    
all_keys[0] # error; not index accessable


# ### Running time comparision

# In[78]:


myList = [(i, i) for i in range(10**5)] # large list of pairs of numbers
myDict = dict(myList)

keys = myDict.keys()

list_keys = list(keys)

get_ipython().run_line_magic('timeit', '900 in keys')

get_ipython().run_line_magic('timeit', '900 in myDict')

get_ipython().run_line_magic('timeit', '900 in list_keys')

get_ipython().run_line_magic('timeit', '0.01 in keys')

get_ipython().run_line_magic('timeit', '0.01 in myDict')

get_ipython().run_line_magic('timeit', '0.01 in list_keys')


# ## Functions -

# In[12]:


def double(x):
    """this is where you put an optional docstring
    that explains what the function does.
    for example, this function multiplies its 
    input by 2"""
    return x * 2

z = double(10) # z is 20
z


# In[ ]:


def my_print(message="my default message"):	
	print (message)

my_print("hello") # prints 'hello'
my_print() # prints 'my default message‘


# In[16]:


def subtract(a=0, b=0):
    return a - b

result = (subtract(10, 5), # returns 5
subtract(0, 5), # returns -5
subtract(b = 5), # same as above
subtract(b = 5, a = 0)) # same as above

print(result)


# In[17]:


# functions are objects too
def double(x): return x * 2
DD = double; # alias for double
DD(2)


# In[19]:


def apply_to_one(f): return f(1) # apply_to_one accepts a function f as input
x=apply_to_one(DD)   
x


# ## Functions – lambda expression

# In[ ]:


y=apply_to_one(lambda x: x+4)


# In[21]:


pairs = [(2, 'two'), (3, 'three'), (1, 'one'), (4, 'four')]
#pairs.sort(key=lambda pair: pair[1]) # sort by second element
pairs.sort(key=lambda pair: abs(pair[0]-2))  # sort by absolute diff between first element and value 2
pairs


# In[51]:


def getKey(pair):
    return pair[0]     # return first element as key
#    return abs(pair[0]-1.5)   # return absolute difference between pair[0] and 1.5 as key
pairs.sort(key=getKey)
pairs


# ## Sorting list

# In[ ]:


x = [4,1,2,3] 
y = sorted(x)     # is [1,2,3,4], x is unchanged 
x.sort()          # now x is [1,2,3,4] 


# In[53]:


x = [-4,1,-2,3]
y = sorted(x, key=abs, reverse=True)  # is [-4,3,-2,1]
x


# In[74]:


# sort the grades from highest count to lowest 
# using an anonymous function
newgrades = sorted(grades.items(), key= lambda pair: pair[0], reverse=False) 

for i, j in grades.items():
    print(i, j)


# ## Map, Reduce, and Filter 

# In[5]:


def double(x): return 2*x 
y = double([2,3]) # what does this do?
y


# In[6]:


y=[[1,2], [2,3]]   
y*4    # what does this do?


# In[25]:


def double(x): return 2*x
b=list(range(5))
double(b)


# In[26]:


b=range(5)
a=list(map(double, b))    # compare with above
a


# In[27]:


b=range(5)
a=list(map(lambda x: 2*x, b))  # equivalent with above. no need to define function double 
a


# In[28]:


b=range(5)
a=map(double, b)
a[0]    # error, a is an iterable but not index-accessible object


# In[29]:


b=range(5)
a=list(map(double, b))
a[0]    # okay now


# In[30]:


from functools import reduce
def myFunc(x, y): return x + y   # simply func that calc sum of two values
reduce(myFunc, range(4))         # apply the function func to the list to compute sum of all values


# In[31]:


from functools import reduce
reduce(lambda x,y: x+y, range(4))  # equivalent to above with lambda func


# In[33]:


from functools import reduce
reduce(lambda x, y: x*y, range(1,11)) # computes 10! 


# ## Zip

# ### conveient to re-org multiple lists (imagine rows & cols in a spreadsheet.)

# In[42]:


list(zip(['a', 'b', 'c'], [1, 2, 3], ['A', 'B', 'C'])) 


# In[41]:


list(zip(['a', 'b', 'c'], [1, 2, 3], ['A', 'B']))  # longer lists truncated


# In[40]:


gradebook = [['James', 'Tom', 'Mary'], [100, 90, 95], ['m', 'm', 'f']]
list(zip(*gradebook))


# In[39]:


gradebook = [['James', 'Tom', 'Mary'], [100, 90, 95], ['m', 'm', 'f']]
list(zip(gradebook[0], gradebook[1], gradebook[2])) # equivalent to above. more tedious

