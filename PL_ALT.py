#############
# Задание 1 #
############# 
n = input("вводите  n ")
m = input("вводите  m ")

#n = 5
#m = 4

i = 1
while True:
    print(i, end='')
    i = 1 + (i + int(m) - 2) % int(n)
    if i == 1:
        break

###########################################
#############
# Задание 2 #
############# 
import sys
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
              return "1"
            elif dist > rad:
              return "2"
            else:
              return "0" #на

if __name__ == "__main__":

        #circle_file = sys.argv[1]
        #point_file = sys.argv[2]
         
        #result = circle(circ_fle, point_fle)
        result = circle()
        print(result)

#############################################################################
#############
# Задание 2 #
############# 

import json

def fill_values(node, value_map):
    """Рекурсивно заполняет поле 'value' в узле и его дочерних элементах."""
    if 'id' in node:
        node_id = node['id']
        if node_id in value_map:
            node['value'] = value_map[node_id]
    
    if 'values' in node:
        for child in node['values']:
            fill_values(child, value_map)


#with open('values.json', 'r') as f1:
#     values_data = json.load(f1)

#with open('tests.json', 'r') as f2:
#     tests_data = json.load(f2)
values_data = {
  "values": [{"id": 2, "value": "passed"}, {"id": 41, "value": "passed"}, 
             {"id": 73, "value": "passed"}, {"id": 110, "value": "failed"}, 
             {"id": 122, "value": "failed"}, {"id": 234, "value": "passed"}, 
             {"id": 238, "value": "passed"}, {"id": 345, "value": "passed"}, 
             {"id": 653, "value": "passed"}, {"id": 690, "value": "failed"}, 
             {"id": 5321, "value": "passed"}, {"id": 5322, "value": "failed"}]
}

tests_data = {
  "tests": [{"id": 2, "title": "Smoke test", "value": ""}, 
            {"id": 41, "title": "Debug test", "value": ""}, 
            {"id": 73, "title": "Performance test", "value": "", 
             "values": [{"id": 345, "title": "Maxperf", "value": "", 
                         "values": [{"id": 230, "title": "Percent", 
                                     "values": [{"id": 234, "title": "200", "value": ""}, 
                                                {"id": 653, "title": "300", "value": ""}]}]}, 
                        {"id": 110, "title": "Stability test", "value": "", 
                         "values": [{"id": 261, "title": "Percent", 
                                     "values": [{"id": 238, "title": "160", "value": ""}, 
                                                {"id": 690, "title": "240", "value": ""}]}]}]}, 
            {"id": 122, "title": "Security test", "value": "", 
             "values": [{"id": 5321, "title": "Confidentiality", "value": ""}, 
                        {"id": 5322, "title": "Integrity", "value": ""}]}]
}


value_map = {item['id']: item['value'] for item in values_data['values']}


for test in tests_data['tests']:
    fill_values(test, value_map)


#with open('report.json', 'w') as f:
#    json.dump(report_data, f, indent=2)
print(tests_data)
##################################################################################
#############
# Задание 4 #
#############
import sys
#nums = sys.argv[1]

#with open('nums.txt', 'r') as file:
    #nums = [line.strip() for line in file]
 
nums = [1, 2, 3, 4]

def minMoves(nums) -> int:
   total_sum = sum(nums)
   min_value = min(nums)
   moves = total_sum - min_value * len(nums)
   return moves
  
print(minMoves( nums))   
 
#######################################
