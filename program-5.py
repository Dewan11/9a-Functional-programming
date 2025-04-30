""" 5.A list contains names of Faculty Members.
Write a program to filter out those names whose length is more
than 8 characters."""

list1=["dewan","arman","Master","himal","shyam singh"] 
print(list(filter(lambda x: len(x)>=8,list1))) 
