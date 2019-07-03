###Problem 1
"""
Implement a group_by_owners function that:
Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
"""""

# def fnc1(dict1):
#     dict2 = {}
#     for i in dict1:
#         if dict1[i] not in dict2:
#             dict2[dict1[i]] = [i]
#         else:
#             dict2[dict1[i]] += [i]
#     return dict2
#
d = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
# print(fnc1(d))

##Problem 2
"""Write a function that checks if a given word is a palindrome. Character case should be ignored."""

# def palindrome(str):
#     rev = ""
#     str1 = str.lower()
#     print(str1)
#     for i in (str1):
#         rev = i + rev
#
#     if rev == str1:
#         print("The string is Palindrome")
#     else:
#         print("The String is Not Palindrome")
#
# palindrome("JkJ")


##Problem 3
"""Write a function to parse a log file & extract details of Errors & Warnings recorded into a separate file."""

# log_file = open('logging.log','r')
# err =open("error.txt",'a')
# warn = open('warning.txt','a')
#
# for line in log_file:
#     if "[error]" in line:
#         err.write(line)
#     elif "[warn]" in line:
#         warn.write(line)


###Problem 4
"""
Write a function that provides change directory(cd) function for an abstract file system.
Notes: Root path is '/'.
The path separator is '/'.
Parent directory is addressable as '..'.
Directory names consist only of English alphabet letters(A - Z and a - z).
The function should support both relative and absolute paths. The function will not be passed any invalid paths. Do not use built - in path - related functions.

For example:
path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)

Output:Should display
'/a/b/c/x'.
"""

# class ChangeDir:
#     def __init__(self, path):
#         self.curr_path = path
#         print(self.curr_path)
#
#     def cd(self, new_path):
#         # i=0;
#         new_path_List=new_path.split('/')
#         path_Length=len(new_path_List)
#         print(new_path)
#         print(path_Length)
#         print(new_path_List)
#         path_List=self.curr_path.split('/')
#         print(path_List)
#         # if new_path_List[0]=='':
#         #     #direct pathname
#         #     del path_List[:]
#         #     path_List.append('/'+new_path_List[1])
#         #     i=i+2
#         # while(i<path_Length):
#         for i in range(path_Length):
#             j=len(path_List)-1
#             if new_path_List[i]=='..':
#                 #parent directory
#                 path_List.pop(j)
#             else:
#                 path_List.append(new_path_List[i])
#             i=i+1
#
#         self.curr_path="/".join(path_List)
#         return self.curr_path
#
# path = ChangeDir('/a/b/c/d')
# path.cd('../x')
# path.cd('/x/y/../z')
# print(path.curr_path) # '/x/z'


### Problem 5:
"""
Design & develop web application to maintain records of students
The single the record shall contain the following information
Name | Roll| Number | Age | Gender |
The application should have the ability to INSERT, DELETE, UPDATE & SEARCH records.
Please Note: this application should not use any DATABASE
"""

# class Db(object):
#     def __init__(self):
#         self.studentlist = []
#
#     def insert(self, Name, Roll, Age, Gen):
#         dict_stu = {}
#         dict_stu["Name"] = Name
#         dict_stu["Roll"] = Roll
#         dict_stu["Age"] = Age
#         dict_stu["Gen"] = Gen
#         self.studentlist.append(dict_stu)
#
#     def delete(self, Roll):
#         for i in self.studentlist:
#             if i["Roll"] == Roll:
#                 self.studentlist.remove(i)
#         return self.studentlist
#
#     def search(self, Roll):
#         searchlist = []
#         for i in self.studentlist:
#             for j in Roll:
#                 if i["Roll"] == j:
#                     searchlist.append(i)
#         return searchlist
#
#     def update(self, Roll, dictupdate):
#         for i in self.studentlist:
#             for j, k in zip(Roll, dictupdate):
#                 list_kys = None
#                 if i["Roll"] == j:
#                     list_kys = list(k.keys())
#                     for key in list_kys:
#                         i[key] = k[key]
#         return self.studentlist
#
#     def display(self):
#         return self.studentlist
#
# db = Db()
#
# db.insert("Rahul", 16, 21, "M")
# db.insert("Anjali", 5, 22, "F")
# db.insert("Priya", 6, 23, "F")
#
# print(db.display())
# #
# db.search([16])
#
# db.update([16], [{"Name": "Shivam"}])
#
# db.delete(5)