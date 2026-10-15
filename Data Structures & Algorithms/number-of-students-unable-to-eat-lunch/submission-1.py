class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        count = 0

        students = deque(students)
        sandwiches = deque(sandwiches)

        while sandwiches and count < n:
            student = students.popleft()
            if student == sandwiches[0]:
                sandwiches.popleft()
                count = 0
                continue
            students.append(student)
            count += 1

        return len(students)
        