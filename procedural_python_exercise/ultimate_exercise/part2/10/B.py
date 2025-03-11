# Create a function that sorts a list of dictionaries by a specific key (e.g., sort students by grades).
def sort_dict_list(list_of_dicts, sort_key, reverse = False):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[sort_key], reverse=reverse)
    return sorted_list

students = [
    {"name": "Jerry", "grade": 80},
    {"name": "Spike", "grade": 85},
    {"name": "Tom", "grade": 90}
]

print(sort_dict_list(students, 'grade', reverse=False))
print(sort_dict_list(students, 'grade', reverse=True))