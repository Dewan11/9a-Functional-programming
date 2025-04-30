#4. Print Palindrome Strings from a List 
 
lst=['madam','plython',"malayalam",12341] 
lst1=filter(lambda x: str(x)==str(x)[::-1],lst) 
print(list(lst1)) 
 
