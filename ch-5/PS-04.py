# what will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after the three operations??
print(s)
print(len(s))# because it says that 20.0 == 20 so one of it will not going to be counted 
