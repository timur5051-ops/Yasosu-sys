# Модуль для интеграции с 1С:Предприятие (упрощённая версия)

class OneCIntegration:
    """Класс для имитации интеграции с 1С"""
    
    @staticmethod
    def export_courses_to_1c(courses):
        """Экспорт курсов в 1С"""
        print("Экспорт курсов в 1С:")
        for course in courses:
            print(f"  Отправка курса: {course[1]} - {course[3]}₽")
        
        print("Данные успешно отправлены в 1С")
        return True
    
    @staticmethod
    def import_students_from_1c():
        """Импорт студентов из 1С (имитация)"""
        print("Импорт студентов из 1С...")
        
        # Имитация данных из 1С
        students_from_1c = [
            {"name": "Алексей Сидоров", "email": "alex@company.com"},
            {"name": "Елена Кузнецова", "email": "elena@company.com"},
            {"name": "Дмитрий Волков", "email": "dmitry@company.com"}
        ]
        
        print(f"Получено {len(students_from_1c)} студентов из 1С")
        return students_from_1c
    
    @staticmethod
    def sync_data():
        """Синхронизация данных между системой и 1С"""
        print("=== Синхронизация с 1С ===")
        print("1. Экспорт курсов в 1С")
        print("2. Импорт студентов из 1С")
        print("3. Обновление статусов платежей")
        print("Синхронизация завершена")

# Пример использования
def demonstrate_integration():
    from db_operations import Database
    
    db = Database()
    
    print("Демонстрация интеграции с 1С:\n")
    
    # 1. Экспорт курсов
    courses = db.read_courses()
    OneCIntegration.export_courses_to_1c(courses)
    
    print("\n" + "="*50 + "\n")
    
    # 2. Импорт студентов из 1С
    students_from_1c = OneCIntegration.import_students_from_1c()
    
    # Добавляем импортированных студентов в нашу БД
    print("\nДобавление студентов из 1С в систему:")
    for student in students_from_1c:
        db.create_student(student["name"], student["email"])
        print(f"  Добавлен: {student['name']}")
    
    print("\n" + "="*50 + "\n")
    
    # 3. Полная синхронизация
    OneCIntegration.sync_data()
    
    db.close()

if __name__ == "__main__":
    demonstrate_integration()