# algorithms.py
# Алгоритмы для системы курсов

# 1. Алгоритм сортировки курсов по цене (пузырьковая сортировка)
def sort_courses_by_price(courses):
    """Сортировка курсов по цене (от дешёвых к дорогим)"""
    n = len(courses)
    for i in range(n):
        for j in range(0, n - i - 1):
            if courses[j].price > courses[j + 1].price:
                courses[j], courses[j + 1] = courses[j + 1], courses[j]
    return courses

# 2. Алгоритм бинарного поиска курса по названию
def find_course_by_name(courses, course_name):
    """Бинарный поиск курса по названию"""
    # Сначала сортируем курсы по названию
    sorted_courses = sorted(courses, key=lambda x: x.title)
    
    low = 0
    high = len(sorted_courses) - 1
    
    while low <= high:
        mid = (low + high) // 2
        current_title = sorted_courses[mid].title
        
        if current_title == course_name:
            return sorted_courses[mid]
        elif current_title < course_name:
            low = mid + 1
        else:
            high = mid - 1
    
    return None

# 3. Алгоритм фильтрации студентов по email домену
def filter_students_by_domain(students, domain):
    """Фильтрация студентов по домену email (например, '@mail.com')"""
    filtered = []
    for student in students:
        if domain in student.email:
            filtered.append(student)
    return filtered

# 4. Алгоритм вычисления средней цены курсов
def calculate_average_price(courses):
    """Вычисление средней цены всех курсов"""
    if not courses:
        return 0
    
    total = 0
    for course in courses:
        total += course.price
    
    return total / len(courses)

# 5. Алгоритм проверки доступности курса (по количеству мест)
def check_course_availability(course, max_students=30):
    """Проверка, есть ли свободные места на курсе"""
    return len(course.students) < max_students