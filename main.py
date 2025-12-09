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

    print("\n6. Использование алгоритмов:")

    from algorithms import sort_courses_by_price, calculate_average_price
    all_courses = [python_course, web_course, data_course]
    courses_copy = all_courses.copy()
    sorted_courses = sort_courses_by_price(courses_copy)

    print("Курсы отсортированы по цене от дешёвых к дорогим")
    for course in sorted_courses:
        print(f" {course.title} {course.price}P")

    avg_price = calculate_average_price(all_courses)
    print(f"\nСредняя цена курса {avg_price:.0f}P")

    from algorithms import check_course_availability

    print("\nДоступность курсов макс 30 студентов")
    for course in all_courses:
        available = check_course_availability(course)
        status = " Свободные места" if available else " Заполнен"
        print(f" {course.title} {status}")

if __name__ == "__main__":
    main()