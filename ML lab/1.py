l1 = list(map(int, input ("Enter a number list : ").split()))
l2 = list(map(int, input ("Enter a number list : ").split()))
print("The Union of the list is : ", list(set(l1) | set(l2)))
print("The Intersection of the list is : ", list(set(l1) & set(l2)))
