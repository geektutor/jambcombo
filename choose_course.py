# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:27:01 2020

@author: johnoyegbite
"""
utme = {
    "civil engineering": ["english", "mathematics", "physics", "chemistry"],
    "computer engineering": ["english", "mathematics", "physics", "chemistry"],
    "electrical engineering": ["english", "mathematics", "physics", "chemistry"],
    "systems engineering": ["english", "mathematics", "physics", "chemistry"],
    "english": ["english", "literature", "christian religious knowledge", "government"],
}

def utme_api():
    return utme



class UTME(object):
    
    def __init__(self):
        # assumes "utme_api()" is the api that returns a JSON format of the UTME 
        # combination with (key: value) => ("%course%": ["%subject 1%", "%subject 2%", ...])
        # key: a string (i.e. a course)
        # value: list of strings (i.e. list of subjects)
        self.__utme = utme_api()
        
        self.__utme_invert = self.__dict_invert()
        
    def __dict_invert(self):
        '''
        self.__utme: a dictionary with immutables values
        returns: the inverse of the dictionary
                
        
        PS: The inverse of self.__utme is another dictionary whose keys are the 
            unique dictionary values in self.__utme.
            The value for a key in the inverse dictionary is a sorted list
            of all keys in self.__utme that have the same value in self.__utme.
            if self.__utme = {1: 10, 6: True, 2: 20, 5: 30, 
                       8: True, 3: 20, 7: True, 4: 30
                       }
            => utme_invert = {10: [1], True: [6, 7, 8], 20: [2, 3], 30: [4, 5]}
        '''
        utme_invert = {}
        for key in self.__utme:
            value = tuple(sorted((self.__utme[key])))
            if value not in utme_invert:
                utme_invert[value] = [key]
            else:
                utme_invert[value] = sorted(utme_invert[value] + [key])
        return utme_invert
    
    def get_combinations_for(self, course):
        """
        type course: str
        rtype: List[str]
        """
        if course in self.__utme:
            return self.__utme[course]
        
        return ["None"] # change to None type if preffered
    
    def get_courses_for(self, combinations):
        """
        type combinations: tuple(str)
        rtype: List[str]
        """
        combinations = tuple(sorted(combinations))
        if combinations in self.__utme_invert:
            return self.__utme_invert[combinations]
        
        return ["None"] # change to None type if preffered
        
if __name__ == "__main__":
    utme = UTME()
    print(utme.get_combinations_for("civil engineering"))
    print()
    print(utme.get_courses_for(["mathematics", "english", "chemistry", "physics"]))