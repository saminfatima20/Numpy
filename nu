import numpy as np

np.random.seed(42)  # for reproducibility
grades = np.random.randint(40, 101, size=(30, 5))  

average_per_student = grades.mean(axis=1)
average_per_subject = grades.mean(axis=0)
overall_average = grades.mean()
highest_grade = grades.max()
lowest_grade = grades.min()

top_students = np.where(average_per_student > 90)[0]
students_with_failing_grades = np.where((grades < 40).any(axis=1))[0]

normalized_grades = (grades - grades.min()) / (grades.max() - grades.min())

print("Average grade per student:\n", average_per_student)
print("\nAverage grade per subject:\n", average_per_subject)
print("\nOverall class average:", overall_average)
print("Highest grade in the class:", highest_grade)
print("Lowest grade in the class:", lowest_grade)
print("\nTop performing students (index):", top_students)
print("Students with any failing grade (index):", students_with_failing_grades)
print("\nNormalized Grades (0-1 scale):\n", normalized_grades.round(2))
