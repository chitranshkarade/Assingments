#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# * = “expressions”
# 'hello' =”values”
# -87.8 = “values”
# -  = “expressions”
# /  = “expressions”
# +	= “expressions”
# 6  =”values”
# 

# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')
Ans- A variable is used to store information , while string is a type of information we store in a variable. Strings contain sets of words enclosed in “ ” .
Ex:-
X = “chitransh”
Here “ X ” is a variable and  “chitransh” is a string .
string “chitransh” is stored in variable ‘X’.


# In[ ]:


3. Describe three different data types.
Ans. Data types in python are categorized as,
1.	Numeric 
2.	Sequence 
3.	Boolean 
4.	Sets
5.	Dictionary           

1.	Numeric data type represent the data which has numeric values, it can be further categorized as,

a.	Integer  ----  a = 12(here ‘a ‘ is a variable and 12 is the numeric value in integer form)
b.	Float --------- a =  12.2 (decimal values are represented by float)
c.	Complex  --  a =  12+2b (complex number is represented by complex class it specified as “real + imaginary part”).

2.	Sequence type  – It is the collection of similar or different types of data ,
a.	String – A string is a collection of one or more characters put in a single quote or double quote. Eg - a =“chitransh” .
b.	List – List are just like array , collectin of different types of data , it can be created by square brackets [ ].
     Eg -  a = [ 123 , 34, “shud” , “chitransh” ]
c.	Tuple – Tuple is just like the list , but it is immutable means its data can’t be  modified once it is created . It can be created by using brackets ( ).
Eg. – a = (23, 34, “chitransh”)

3.	Boolean -Data type with one of the two built in values as , true or false .


# In[2]:


''' 4.	What is an expression made up of? What do all expressions do?
Ans. An expression is a combination of operators and operands that is interpreted to produce some other value.
for example:-
'''

a = 20 # operands
b=  10
c= a+b # expresion (where "+" is an operator)
print(c)
print(a*b)
print(a/b)
print(a-b)


# In[ ]:


get_ipython().set_next_input('5. This assignment statements, like spam = 10. What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')
Ans.As explained ealier,  
    An expression is a combination of operators and operands that is interpreted to produce some other value.
    and the statement is just like a command that a python interpreter executes like print.


# In[3]:


# for example--

a = 20 # operands
b=  10
c= a+b # expresion (where "+" is an operator)
print(c) # print is a statement


# In[ ]:


get_ipython().set_next_input('6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1
Ans:- output will be 23


# In[8]:


bacon = 22
bacon + 1


# In[ ]:


get_ipython().set_next_input('7. What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')
'spam' + 'spamspam'  = ans :- ‘spamspamspam’
'spam' * 3    = ans:- ‘spamspamspam’


# In[9]:


# execution 
'spam' + 'spamspam'


# In[10]:


'spam' * 3


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')
Ans :- Variable names can be alphanumeric, and casesensitive .But Variable name cannot start with a number, even spaces and '-' is also not allowed.
       some examples of valid variable names are- chit1 , chit , chit_1 ,Chit , Chit_2
    Therefore egg is a valid variable name but 100 is not.


# In[ ]:


get_ipython().set_next_input('9. What three functions can be used to get the integer, floating-point number, or string version of a value');get_ipython().run_line_magic('pinfo', 'value')
Ans. Three functions are as follows 
string        =  str()
integer       =  int()
floating type =  float()


# In[ ]:


get_ipython().set_next_input('10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten ' + 99 + ' burritos.'
Ans. As we have learned same type of data can be manupulated using operators.
     in this case we are adding string to a no. so we have to convert interger or number into a string with ( " " or ' ').
    for example:-     


# In[11]:


'I have eaten ' + '99' + ' burritos.'


# In[ ]:





# In[ ]:




