from course import Course
from student import Student

def main():
    print("=== СИСТЕМА ОРГАНИЗАЦИИ КУРСОВ ===\n")
    
    python_course = Course("Python для начинающих", 40, 15000)
    web_course = Course("Веб-разработка", 60, 20000)
    data_course = Course("Анализ данных", 50, 18000)
    
    student1 = Student("Иван Иванов", "ivan@mail.com")
    student2 = Student("Мария Петрова", "maria@mail.com")
    
    print("1. Созданные курсы:")
    print(python_course.get_info())
    print(web_course.get_info())
    print(data_course.get_info())
    
    print("\n2. Запись студентов на курсы:")
    student1.enroll(python_course)
    student1.enroll(web_course)
    student2.enroll(data_course)
    
    print("\n3. Информация о студентах:")
    print(student1.get_info())
    print(student2.get_info())
    
    print("\n4. Статистика:")
    python_course.show_students()
    web_course.show_students()
    data_course.show_students()
    
    print("\n5. Курсы студентов:")
    student1.show_courses()
    student2.show_courses()

if __name__ == "__main__":
    main()