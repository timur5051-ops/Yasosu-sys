from db_operations import Database
from logger import log_info, log_error

def test_with_errors():
    db = Database()
    
    log_info("Начало тестирования", "debug_test")
    
    print("1. Тест: создание курса с некорректной ценой")
    try:
        db.create_course("Тестовый курс", -10, -1000)
    except Exception as e:
        log_error(f"Ошибка: {str(e)}", "debug_test")
        print(f"   Обнаружена ошибка: {e}")
    
    print("\n2. Тест: создание студента с одинаковым email")
    db.create_student("Тест1", "test@mail.com")
    try:
        db.create_student("Тест2", "test@mail.com")
    except Exception as e:
        log_error(f"Ошибка: {str(e)}", "debug_test")
        print(f"   Обнаружена ошибка: {e}")
    
    print("\n3. Тест: запись на несуществующий курс")
    try:
        db.enroll_student(999, 999)
    except Exception as e:
        log_error(f"Ошибка: {str(e)}", "debug_test")
        print(f"   Обнаружена ошибка: {e}")
    
    db.close()
    log_info("Тестирование завершено", "debug_test")
    print("\nТестирование завершено. Лог в app_debug.log")

if __name__ == "__main__":
    test_with_errors()