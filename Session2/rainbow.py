rainbow = ['green', 'orange', 'violet']
position_violet = rainbow.index('violet')
rainbow.insert(position_violet,'red')
print(rainbow)

rainbow.append('yellow')
print(rainbow)

rainbow.reverse()
print(rainbow)

rainbow.remove('orange')
print(rainbow)