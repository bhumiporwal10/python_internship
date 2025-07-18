import matplotlib.pyplot as plt

semesters = ['Sem 1', 'Sem 2', 'Sem 3']
cgpa = [9.7, 9.07, 9.57]

plt.figure(figsize=(6, 4))
plt.plot(semesters, cgpa, marker='o', linestyle='--', color='purple')
plt.title('Semester-wise Result')
plt.xlabel('Semester')
plt.ylabel('Marks')
plt.grid(True)
plt.show()
