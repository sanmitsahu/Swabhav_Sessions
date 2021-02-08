def add(a,b):
	print(f'{a:,.2f} + {b:,.2f} = {a+b :>15,.2f}')

def foo(a,b):
	print(a,b)

shares = (10000.567,10000.567)
#add(shares)
add(*shares)
add(*[10000.567,10000.567])
foo(*'Hi')