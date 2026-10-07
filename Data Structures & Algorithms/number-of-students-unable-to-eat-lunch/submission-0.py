class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        if len(sandwiches) <= 0 or len(students) <= 0:
            return -1

        num_iter = 0
        while sandwiches and students and num_iter <= n:
            curr_sandwich = sandwiches[0]
            curr_student = students[0] # for 0

            if curr_student == curr_sandwich:
                # we got a match, take it and leave
                sandwiches = sandwiches[1:]
                students = students[1:]
                num_iter = 0
            else:
                # no match - get student to the back of the queue
                students = students[1:]
                students.append(curr_student)
                num_iter += 1

        return len(students)

        