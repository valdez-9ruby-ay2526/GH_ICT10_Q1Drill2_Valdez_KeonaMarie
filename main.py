# String Formatting
from pyscript import display, document

student_name = 'Keona Marie Valdez' #String
age = 15 #Integer
height14 = 157.48 #Float-point
countries_ = ['Korea, USA, Singapore'] #List
student_type = False #Boolean
color_dict = {'color': 'Tiffany Blue'} #Dictionary
car_brand = {'car brand': 'BMW'} #Dictionary
shoe_size = {'shoe size': '8'} #Dictionary
best_friend = {'best friend': 'Gurleen'} #Dictionary
fav_fruits =  {'Watermelon', 'Grapes', 'Dragon fruit', 'Banana', 'Mango'} #Set
seven_days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') #Tuple


display(f'Hello! My name is <i>{student_name}</i>. I am {age} years old. My height is {height14} cm.', target='result')
document.getElementById('result').innerHTML = f'Hello! My name is <i>{student_name}</i>. I am {age} years old and my height is {height14} cm. I want to visit {countries_}. I am a new student: {student_type}. My favorite color is {color_dict["color"]}. My favorite car brand is {car_brand["car brand"]}. My shoe size is {shoe_size["shoe size"]}. My best friend is {best_friend["best friend"]}. My favorite fruits are {fav_fruits}. The days of the week are {seven_days_week}.'