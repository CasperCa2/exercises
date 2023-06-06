

def linear_search(students, id):
    return next((student for student in students if student.id == id), None)


def binary_search(students, id):
    left = 0
    right = len(students)

    while left < right:
        mid = (left+right) // 2
        middle_id = students[mid].id
        if id < middle_id:
            right = mid
        elif id > middle_id:
            left = mid + 1
        else:
            return students[mid]

    return None
