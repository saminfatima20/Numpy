# Average score per student
student_averages = np.mean(scores, axis=1)
subject_averages = np.mean(scores, axis=0)

highest_score = np.max(scores)
lowest_score = np.min(scores)

top_student_index = np.argmax(student_averages)
top_student = students[top_student_index]

top_subject_index = np.argmax(subject_averages)
top_subject = subjects[top_subject_index]

print("Average score per student:")
for name, avg in zip(students, student_averages):
    print(f"{name}: {avg:.2f}")

print("\nAverage score per subject:")
for subject, avg in zip(subjects, subject_averages):
    print(f"{subject}: {avg:.2f}")

print(f"\nHighest score in the class: {highest_score}")
print(f"Lowest score in the class: {lowest_score}")
print(f"Top-performing student: {top_student}")
print(f"Subject with highest class average: {top_subject}")
