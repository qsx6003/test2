a=input("第一行字")
b=input("第二行字")
c=input("第三行字")
x=len(a)
y=len(b)
z=len(c)
m=x
if m>y:
	m=y
if z>m:
	m=z
print("+", ("-"*(m+2)), "+")
print("|", a.center(m+2), "|")
print("|", b.center(m+2), "|")
print("|", c.center(m+2), "|")
print("+", ("-"*(m+2)), "+")

