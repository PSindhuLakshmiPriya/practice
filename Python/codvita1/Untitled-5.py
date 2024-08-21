# Read input
C, N = map(int, input().split())
quota = list(map(int, input().split()))
students = []

for _ in range(N):
    data = input().split(", ")
    student_id = data[0]
    percentage = float(data[1])
    choices = data[2:]

    students.append((student_id, percentage, choices))

# Initialize college data
colleges = {f'C-{i + 1}': [] for i in range(C)}

# Allocate students to colleges in round 1
for student in students:
    student_id, percentage, choices = student
    for choice in choices:
        college = colleges[choice]
        if len(college) < quota[C - 1]:
            college.append((student_id, percentage))
            break

# Sort and calculate cut-off percentages
cut_offs = []
for college, students in colleges.items():
    if students:
        students.sort(key=lambda x: (-x[1], x[0]))  # Sort by percentage and then by student_id
        cut_offs.append((college, students[-1][1]))
    else:
        cut_offs.append((college, "n/a"))

# Sort cut-off percentages in descending order
cut_offs.sort(key=lambda x: (-x[1], x[0]))

# Print the cut-off percentages
for cut_off in cut_offs:
    print(f"{cut_off[0]} {cut_off[1]}")
