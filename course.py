class Course:
    """Класс для представления курса"""
    
    def __init__(self, title, duration, price):
        self.title = title
        self.duration = duration  
        self.price = price
        self.students = []  
    
    def add_student(self, student_name):
        """Добавить студента на курс"""
        self.students.append(student_name)
        print(f"Студент {student_name} добавлен на курс '{self.title}'")
    
    def get_info(self):
        """Получить информацию о курсе"""
        return f"Курс: {self.title}, Длительность: {self.duration}ч, Цена: {self.price}₽"
    
    def show_students(self):
        """Показать всех студентов курса"""
        if self.students:
            print(f"Студенты курса '{self.title}':")
            for student in self.students:
                print(f"  - {student}")
        else:
            print(f"На курсе '{self.title}' пока нет студентов")