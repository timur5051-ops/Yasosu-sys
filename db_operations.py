import sqlite3
from logger import log_error, log_info, log_debug

class Database:
    def __init__(self, db_name='courses.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    # CRUD операции для курсов
    def create_course(self, title, duration, price):
        try:
            log_info(f"Создание курса: {title}", "db_operations")
            self.cursor.execute(
                "INSERT INTO courses (title, duration, price) VALUES (?, ?, ?)",
                (title, duration, price)
            )
            self.conn.commit()
            course_id = self.cursor.lastrowid
            log_info(f"Курс создан, ID: {course_id}", "db_operations")
            return course_id
        except Exception as e:
            log_error(f"Ошибка при создании курса: {str(e)}", "db_operations")
            return None
    
    def read_courses(self):
        try:
            log_debug("Чтение списка курсов", "db_operations")
            self.cursor.execute("SELECT * FROM courses")
            courses = self.cursor.fetchall()
            log_info(f"Получено {len(courses)} курсов", "db_operations")
            return courses
        except Exception as e:
            log_error(f"Ошибка при чтении курсов: {str(e)}", "db_operations")
            return []
    
    def update_course(self, course_id, title=None, duration=None, price=None):
        try:
            updates = []
            values = []
            
            if title:
                updates.append("title = ?")
                values.append(title)
            if duration:
                updates.append("duration = ?")
                values.append(duration)
            if price:
                updates.append("price = ?")
                values.append(price)
            
            if updates:
                values.append(course_id)
                query = f"UPDATE courses SET {', '.join(updates)} WHERE id = ?"
                log_info(f"Обновление курса ID {course_id}", "db_operations")
                self.cursor.execute(query, values)
                self.conn.commit()
                log_info(f"Курс ID {course_id} обновлён", "db_operations")
        except Exception as e:
            log_error(f"Ошибка при обновлении курса: {str(e)}", "db_operations")
    
    def delete_course(self, course_id):
        try:
            log_info(f"Удаление курса ID {course_id}", "db_operations")
            self.cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
            self.conn.commit()
            log_info(f"Курс ID {course_id} удалён", "db_operations")
        except Exception as e:
            log_error(f"Ошибка при удалении курса: {str(e)}", "db_operations")
    
    # CRUD операции для студентов
    def create_student(self, name, email):
        try:
            log_info(f"Создание студента: {name}", "db_operations")
            self.cursor.execute(
                "INSERT INTO students (name, email) VALUES (?, ?)",
                (name, email)
            )
            self.conn.commit()
            student_id = self.cursor.lastrowid
            log_info(f"Студент создан, ID: {student_id}", "db_operations")
            return student_id
        except Exception as e:
            log_error(f"Ошибка при создании студента: {str(e)}", "db_operations")
            return None
    
    def read_students(self):
        try:
            log_debug("Чтение списка студентов", "db_operations")
            self.cursor.execute("SELECT * FROM students")
            students = self.cursor.fetchall()
            log_info(f"Получено {len(students)} студентов", "db_operations")
            return students
        except Exception as e:
            log_error(f"Ошибка при чтении студентов: {str(e)}", "db_operations")
            return []
    
    # Запись студента на курс
    def enroll_student(self, student_id, course_id):
        try:
            log_info(f"Запись студента {student_id} на курс {course_id}", "db_operations")
            self.cursor.execute(
                "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
                (student_id, course_id)
            )
            self.conn.commit()
            log_info(f"Студент {student_id} записан на курс {course_id}", "db_operations")
        except Exception as e:
            log_error(f"Ошибка при записи на курс: {str(e)}", "db_operations")
    
    # Получение курсов студента
    def get_student_courses(self, student_id):
        try:
            log_debug(f"Получение курсов студента {student_id}", "db_operations")
            self.cursor.execute('''
                SELECT c.id, c.title, c.duration, c.price 
                FROM courses c
                JOIN enrollments e ON c.id = e.course_id
                WHERE e.student_id = ?
            ''', (student_id,))
            courses = self.cursor.fetchall()
            log_info(f"Получено {len(courses)} курсов для студента {student_id}", "db_operations")
            return courses
        except Exception as e:
            log_error(f"Ошибка при получении курсов студента: {str(e)}", "db_operations")
            return []
    
    # Получение студентов курса
    def get_course_students(self, course_id):
        try:
            log_debug(f"Получение студентов курса {course_id}", "db_operations")
            self.cursor.execute('''
                SELECT s.id, s.name, s.email 
                FROM students s
                JOIN enrollments e ON s.id = e.student_id
                WHERE e.course_id = ?
            ''', (course_id,))
            students = self.cursor.fetchall()
            log_info(f"Получено {len(students)} студентов для курса {course_id}", "db_operations")
            return students
        except Exception as e:
            log_error(f"Ошибка при получении студентов курса: {str(e)}", "db_operations")
            return []
    
    def close(self):
        log_info("Закрытие соединения с БД", "db_operations")
        self.conn.close()

# Тестовые операции
def test_database():
    db = Database()
    
    print("1. Создаём курсы:")
    course1 = db.create_course("Python для начинающих", 40, 15000)
    course2 = db.create_course("Веб-разработка", 60, 20000)
    print(f"   Созданы курсы с ID: {course1}, {course2}")
    
    print("\n2. Создаём студентов:")
    student1 = db.create_student("Иван Иванов", "ivan@mail.com")
    student2 = db.create_student("Мария Петрова", "maria@mail.com")
    print(f"   Созданы студенты с ID: {student1}, {student2}")
    
    print("\n3. Записываем студентов на курсы:")
    db.enroll_student(student1, course1)
    db.enroll_student(student1, course2)
    db.enroll_student(student2, course1)
    print("   Записи созданы")
    
    print("\n4. Читаем все курсы:")
    courses = db.read_courses()
    for course in courses:
        print(f"   ID: {course[0]}, Название: {course[1]}, Цена: {course[3]}₽")
    
    print("\n5. Курсы студента Ивана:")
    student_courses = db.get_student_courses(student1)
    for course in student_courses:
        print(f"   - {course[1]}")
    
    db.close()
    print("\nТестирование завершено!")

if __name__ == "__main__":
    test_database()