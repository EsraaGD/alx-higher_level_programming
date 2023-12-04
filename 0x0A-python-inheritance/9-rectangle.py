#!/usr/bin/python3
class Rectangle(BaseGeometry):
     def __init__(self, width, height):
        """inherits from BaseGeometry"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height
    
    def __str__(self):       
        return f"[Rectangle] {self.__width/self.__height}"