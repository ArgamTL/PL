import json

'''
val_file = input("Enter the path to the values.json")
test_file  = input("Enter the path to the tests.json")
 
with open(val_file, 'r') as f1:
     values_data = json.load(f1)

with open(test_file, 'r') as f2:
     tests_data = json.load(f2)
'''


def fill_values(node, value_map):
    if 'id' in node:
        node_id = node['id']
        if node_id in value_map:
            node['value'] = value_map[node_id]
    
    if 'values' in node:
        for child in node['values']:
            fill_values(child, value_map)
# data for fast testing 

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

report_data = json.loads(json.dumps(tests_data))

for test in report_data['tests']:
    fill_values(test, value_map)

with open('report.json', 'w') as f:
    json.dump(report_data, f, indent=2)

#print for testing
print(report_data)   
    
