# Простые тесты для системы курсов

from course import Course
from student import Student
from algorithms import sort_courses_by_price, calculate_average_price

def test_course_creation():
    """Тест создания курса"""
    print("1. Тест создания курса:")
    course = Course("Тестовый курс", 40, 15000)
    assert course.title == "Тестовый курс"
    assert course.duration == 40
    assert course.price == 15000
    print("   ✓ Курс создан корректно")
    
    # Тест с некорректными данными
    try:
        Course("", -10, -1000)
        print("   ✗ Ошибка: курс с некорректными данными создан")
    except:
        print("   ✓ Некорректные данные отклонены")
    print()

def test_student_creation():
    """Тест создания студента"""
    print("2. Тест создания студента:")
    student = Student("Иван Тестов", "test@mail.com")
    assert student.name == "Иван Тестов"
    assert student.email == "test@mail.com"
    print("   ✓ Студент создан корректно")
    print()

def test_enrollment():
    """Тест записи на курс"""
    print("3. Тест записи на курс:")
    course = Course("Курс для записи", 30, 10000)
    student = Student("Студент", "student@mail.com")
    
    student.enroll(course)
    assert len(student.courses) == 1
    assert len(course.students) == 1
    print("   ✓ Запись на курс выполнена")
    print()

def test_sorting_algorithm():
    """Тест алгоритма сортировки"""
    print("4. Тест алгоритма сортировки:")
    courses = [
        Course("Дорогой", 10, 30000),
        Course("Дешёвый", 10, 5000),
        Course("Средний", 10, 15000)
    ]
    
    sorted_courses = sort_courses_by_price(courses)
    assert sorted_courses[0].price == 5000
    assert sorted_courses[1].price == 15000
    assert sorted_courses[2].price == 30000
    print("   ✓ Сортировка работает корректно")
    print()

def test_average_price():
    """Тест расчёта средней цены"""
    print("5. Тест расчёта средней цены:")
    courses = [
        Course("Курс 1", 10, 10000),
        Course("Курс 2", 10, 20000),
        Course("Курс 3", 10, 30000)
    ]
    
    avg = calculate_average_price(courses)
    assert avg == 20000
    print(f"   ✓ Средняя цена рассчитана: {avg}₽")
    print()

def test_empty_data():
    """Тест работы с пустыми данными"""
    print("6. Тест работы с пустыми данными:")
    
    # Пустой список курсов
    empty_courses = []
    avg = calculate_average_price(empty_courses)
    assert avg == 0
    print("   ✓ Средняя цена для пустого списка: 0")
    print()

def run_all_tests():
    """Запуск всех тестов"""
    print("=" * 50)
    print("ЗАПУСК ТЕСТОВЫХ СЦЕНАРИЕВ")
    print("=" * 50)
    
    tests = [
        test_course_creation,
        test_student_creation,
        test_enrollment,
        test_sorting_algorithm,
        test_average_price,
        test_empty_data
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"   ✗ Тест не пройден: {e}")
    
    print("=" * 50)
    print(f"ИТОГ: {passed}/{total} тестов пройдено успешно")
    print("=" * 50)
    
    if passed == total:
        print("✅ Все тесты пройдены успешно!")
    else:
        print(f"⚠️  {total - passed} тестов не пройдено")

if __name__ == "__main__":
    run_all_tests()