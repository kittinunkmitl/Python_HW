from person_utils import age
import  person_module

p1 = {"fname": "pang", "lname": "lamun", "dob": '1990-09-19'}
print(p1['fname'], p1['lname'], str(age(p1['dob'])))
print(p1['fname'], p1['lname'], str(person_module.age(p1['dob'])))


# print(std1['sid'], std1['fullname'])
# print( 'name' in std1.keys() )

# std_heights = list()
std_heights = [175, 165, 157, 171, 166]
# print(std_heights[1])
# std_heights.append(181)
# std_heights = std_heights + [151,155]
# print(std_heights)
# print("Total : ", sum(std_heights))
# print("Average : ", sum(std_heights) / len(std_heights))
# print(std_heights)
