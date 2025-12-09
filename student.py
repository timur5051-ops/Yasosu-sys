class Student:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.courses = []
    
    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self.name)
        print(f"{self.name} записан на курс '{course.title}'")
    
    def get_info(self):
        return f"Студент: {self.name}, Email: {self.email}"
    
    def show_courses(self):
        if self.courses:
            print(f"Курсы студента {self.name}:")
            for course in self.courses:
                print(f"  - {course.title}")
        else:
            print(f"Студент {self.name} пока не записан на курсы")