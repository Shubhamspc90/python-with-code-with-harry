#format() and fstring

template='''Dear {}, You are awesome.
take this {}$ bag'''

a="Shubham"
a1=100
b="dhar"
b1=200
c="Varun"
c1=1000


s1=r=template.format(a,a1)
print(s1)

s2=r=template.format(b,b1)
print(s2)

# or directly 
print(f"Dear {c}, you are awesome, Take this {c1}$ bag. ")