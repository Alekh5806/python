subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

# Convert the list to a set to get only unique subjects
unique_subjects = set(subjects)

# Number of classrooms needed = number of unique subjects
print("Number of classrooms needed:", len(unique_subjects))