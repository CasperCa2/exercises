def process_data(string_data):
    students = {}

    for item in string_data:
        name, age, *courses = item.split(',')
        students[name] = {"age": int(age), "courses": courses}

    return students


def average_age(data):
    age_total = 0
    total_student = 0
    for v in data.values():
        age_total += v["age"]
        total_student += 1
    return age_total / total_student


def courses(data):
    courses_set = set()
    for v in data.values():
        courses_set.update(v["courses"])

    return courses_set


def most_common_courses(data):
    courses = {}
    for student in data.values():
        for course in student["courses"]:
            if course not in courses:
                courses[course] = 0
            courses[course] += 1
    max_count = max(courses.values())
    return {
        course
        for course in courses.keys()
        if courses[course] == max_count
    }
