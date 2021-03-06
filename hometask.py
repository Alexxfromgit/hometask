# created a file

names = ['Ann', 'Bob', 'Suzan', 'Radonir', 'Fill', 'Sam', 'Al']
ages = [12, 33, 56, 87, 4, 18, 21]
text_a = "Special cases aren't special enough to break the rules."
text_b = "In the face of ambiguity, refuse the temptation to guess."

'''1. Посчитать количество элементов в списке names'''
print(len(names))

'''2. Посчитать количество элементов в списке ages'''
print(len(ages))

'''3. Посчитать количество элементов в строке text_a'''
print(len(text_a))

'''4. Посчитать количество элементов в строке text_b'''
print(len(text_b))

'''5. Посчитать сумму элементов списка ages'''
print(sum(ages))

'''6. Вывести максимальный элемент списка ages'''
print(max(ages))

'''7. Вывести минимальный элемент списка ages'''
print(min(ages))

'''8. Найти самое короткое слово в text_a'''
print(min(text_a.split(), key=len))

'''9. Найти самое длинное слово в text_b'''
text_b = text_b.replace(',','')
print(max(text_b.split(), key=len))

'''10. Вывести слово special из text_a'''
if text_a.find('special') != 1:
  print('special')
  
'''11. Вывести слово refuse из text_b'''
if text_b.find('refuse') != 1:
  print('refuse')

'''12. В names и ages имена соответствуют возрасту,
      используя print вывести имя и возраст, например
      Sergey is 19 yesrs old
      то есть Sergey и 19 взяты из списков'''
i = 0
while i <= len(names) and i <= len(ages):
  print(names[i], ' is', str(ages[i]), ' years old')
  i += 1

  
