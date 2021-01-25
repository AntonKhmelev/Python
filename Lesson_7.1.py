# задание 1
import numpy as np

class Matrix:
      def __init__(self, name):
          self.name = name

      def __str__(self):
          return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.name]))

# не сообразил с синтаксисом, как правильно сложить две матрицы в одну. Общая идея такая, что идем циклом for
# в содержимое первого списка (for i in self.name), где элемент это список
# из каждого списка вытаскиваем уже элементы (for j in i)
# далее идем во второй список (for k in self.other), прочесываем вложенные списки
# выбираем из вложенных списков также по элементу (for l in k:)
# наконец, складываем друг с другом перебранные элементы в нужном порядке в новую матрицу-список (return self.name[i][j] + other[k][l])
# а слепить это все в работающий алгоритм уже не получилось, запутался...

      #def __add__(self):
         # matr = [[0,0,0],
                #  [0,0,0],
               #   [0,0,0]]

       #def __add__(self):
        #   self.matr = []
         #  i = 0
       #for i in range(len(self.name)):
        #   self.matr.append(i)
         #  i += 1
          # return self.matr
           #for j in range(len(self.name[i])):

             #     matr[i][j] = self.mat1[i][j] + self.mat2[i][j]
               #   return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

          #self.other = other
          #self.name = name
           # for i in self.name:
            #  for j in i:
             #   for k in self.other:
              #    for l in k:
               #     return self.name[i][j] + other[k][l]

#my_matr = Matrix([[1,2,6],
                 # [3,4,7],
                #  [5,6,8]],
                # [[7,-3,0],
                  #[25,100,-10],
                 # [5,11,-45]])
matr1 = Matrix([[1,2,6],[3,4,7],[5,6,8]])

matr2 = Matrix([[7,-3,0],[25,100,-10],[5,11,-45]])

print(matr1)
print(matr2)

#print(matr2)

#print(matr1 + matr2)

#print()




   # def array(self):
   #     f = []
   #     return ([[self.rows,self.cols]*2, [self.rows,self.cols]*2])

   # def __str__(self):
   #     return f'Строковое представление {self.array}'



#a = Matrix(3,4)

#print(a.array())
#print(a.__str__())

