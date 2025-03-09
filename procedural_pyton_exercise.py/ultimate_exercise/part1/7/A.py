def top_student(x):
    if not x:
        return []
    
    max_score = max(x.values())

    top_students = [name for name, result in x.items() if result == max_score]
    return top_students

scores = {
    'Alice': 95,
    'Bob': 85,
    'Charlie': 95,
    'David': 90
}

result = top_student(scores)
print("Top student(s):", result)