# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13mnvNvHHB6KTkh3Vnps1O0vckdKoA1mS
"""

#Project-Description:  Email slicer is just a simple tool that will take multiple email 
#        address as an input and slice it to produce the username and the domain
#        associated with it. The email must be divided into two strings by using '@' 
#        as the separator.

#CODE:
print("\nWELCOME:)\n")
n = int(input("How many Emails you wants to Slice: "))
for i in range (1,n+1):
  n=str(input("\nEmail: "))
  l=len(n)
  d=0
  for i in range(1,l):
    if n[i]=='@':
      d=i
      break
  if d>0:
    a=""
    for i in range(0,d):
      a+=n[i]
    print("User Name: ",a,end="")
    q = ""
    for j in range(d+1,len(n)):
      q+=n[j]
    print("\nDomain:",q,end="",)
    print()
  print("\nThank you :)")