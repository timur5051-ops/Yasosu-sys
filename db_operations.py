import sqlite3

class Database:
    def __init__(self, db_name='courses.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    # CRUD операции для курсов
    def create_course(self, title, duration, price):
        self.cursor.execute(
            "INSERT INTO courses (title, duration, price) VALUES (?, ?, ?)",
            (title, duration, price)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def read_courses(self):
        self.cursor.execute("SELECT * FROM courses")
        return self.cursor.fetchall()
    
    def update_course(self, course_id, title=None, duration=None, price=None):
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
            self.cursor.execute(query, values)
            self.conn.commit()
    
    def delete_course(self, course_id):
        self.cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        self.conn.commit()
    
    # CRUD операции для студентов
    def create_student(self, name, email):
        self.cursor.execute(
            "INSERT INTO students (name, email) VALUES (?, ?)",
            (name, email)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def read_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()
    
    # Запись студента на курс
    def enroll_student(self, student_id, course_id):
        self.cursor.execute(
            "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
            (student_id, course_id)
        )
        self.conn.commit()
    
    # Получение курсов студента
    def get_student_courses(self, student_id):
        self.cursor.execute('''
            SELECT c.id, c.title, c.duration, c.price 
            FROM courses c
            JOIN enrollments e ON c.id = e.course_id
            WHERE e.student_id = ?
        ''', (student_id,))
        return self.cursor.fetchall()
    
    # Получение студентов курса
    def get_course_students(self, course_id):
        self.cursor.execute('''
            SELECT s.id, s.name, s.email 
            FROM students s
            JOIN enrollments e ON s.id = e.student_id
            WHERE e.course_id = ?
        ''', (course_id,))
        return self.cursor.fetchall()
    
    def close(self):
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