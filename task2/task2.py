#############
# Задание 2 #
############# 
import math

def circle(circ_fle = [1.0, 2.0, 4.0], point_fle = [3.5, 4.0]):
  
    
        #with open(circ_fle, 'r') as f:
            #circ_fle = f.readline().strip().split()
            center_x, center_y, rad = map(float, circ_fle)

        #with open(point_fle, 'r') as f:
            #point_fle = f.readline().strip().split()
            point_x, point_y = map(float, point_fle)
            
            dist = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2)
            if dist < rad:
              return "1" #точка внутри
            elif dist > rad:
              return "2" #точка снаружи.
            else:
              return "0" #точка лежит на окружности

if __name__ == "__main__":
  
  circ_fle = input("Вводите файл с координатами и радиусом окружности")
  point_fle  = input("Вводите файл с координатами точек")
  #result = circle(circ_fle, point_fle)
  result = circle()
  print(result)
