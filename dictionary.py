students = [
{"id":1, "details": {"name": "John", "age":25,"gender":"Male","courses":["Math","Science"]}},
{"id":2, "details": {"name": "Jane", "age":20,"gender":"female","courses":["Math","Science"]}},
{"id":3, "details": {"name": "Tom", "age":22,"gender":"Male","courses":["Math","Kiswahili"]}}
]

for student in students:
    print("-----------------------------------------------")
    print(student["id"])
    print(student["details"]["name"])
    print(student["details"]["age"])
    print(student["details"]["gender"])
    for course in student["details"]["courses"]:
        print("\t" + course)
    print("\n")
    print("-----------------------------------------------")
