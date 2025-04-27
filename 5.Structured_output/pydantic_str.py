# Pydantic is a data validation and data parisng library in python 
# it ensure we work with the data which is correct structued and type safe
"""Things and points to learn in here (provided by pydantic) Basic eg, default values, Optional fields,
coerce , build in validation, field func(using this we can set default values, constraints, description, regex expressions)
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional 

# isse ye hoga ki if string ki jagah kuch aur aaya to it will throw and error.

class Student(BaseModel):
    name: str =  'Danish'  #here we gave default value to name can also be passed in object
    age: Optional[int] = None 
    email: EmailStr 
    cgpa: float = Field(gt=0, lt=10, description= 'Ye decimal rep hai student ke cgpa ka') #also we can give default cgpa here using 'default=num'


# we created a dict but why?
new_student = {'age': 22, 'email': 'afdf@gmail.com ', 'cgpa': 1}

student = Student(**new_student)
print(student)