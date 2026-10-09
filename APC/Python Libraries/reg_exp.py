import re
p=re.compile('[a-e]')
a="Python is a programming language"
a1="Python is a 123programming @language"

print("\nre.compile & re.findall for [a-e]:")
print(p.findall(a))


b=re.sub("\s+","-",a)
print("\nre.sub:")
print(b)

c=re.split("m",a)
print("\nre.split:")
print(c)

d=re.escape(a)
print("\nre.escape:")
print(d)

e=re.search("a",a)
print("\nre.search",e)

print("\n",re.sub("\d+","digit_",a1))

print("\n",re.sub("\D+","digit_",a1))

print(re.search("\bPython",a1))

f=re.escape(a1)
print("\nre.escape:")
print(f)