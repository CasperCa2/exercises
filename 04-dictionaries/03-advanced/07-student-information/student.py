# Write your code here


def process_data(string_data):
    new_dictionary = {}
    for item in string_data:
        name, age, *courses = item.split(",")
        new_dictionary[name] = {
            "age": int(age),
            "courses": courses
        }
    return new_dictionary


def average_age(data):
    sum = 0
    num_student = 0
    for student in data.values():
        sum += student["age"]
        num_student += 1
    average_age = sum / num_student
    return average_age


def courses(data):

    for value in data.values():
        value_courses = value["courses"]
    return set(value_courses)


def most_common_courses(data):
    new_dict = {}

    for value in data.values():
        if value["Math"]
        new_dict.update(value["courses"])
