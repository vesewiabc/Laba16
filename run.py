from flask import Flask

app = Flask(__name__)

# Модель студента
class Student:
    def __init__(self, id, first_name, last_name, email, group, grades):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.group = group
        self.grades = grades

# Тестовые данные
students = [
    Student(1, "Иван", "Иванов", "ivanov@edu.ru", "ИСП-34", {"Математика": 5, "Программирование": 4, "Базы данных": 5}),
    Student(2, "Мария", "Петрова", "petrova@edu.ru", "ИСП-34", {"Математика": 4, "Программирование": 5, "Базы данных": 4})
]

@app.route('/')
def index():
    student = students[0]  # Первый студент для примера
    
    html = f'''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Личный кабинет студента</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f0f2f5;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 800px;
                margin: 0 auto;
            }}
            .header {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                text-align: center;
                margin-bottom: 20px;
            }}
            .welcome-message {{
                font-size: 2em;
                color: #2c3e50;
                margin-bottom: 10px;
            }}
            .profile-card, .grades-card {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }}
            .profile-info p {{
                margin: 10px 0;
                padding: 8px;
                background: #f8f9fa;
                border-radius: 5px;
            }}
            .grade-item {{
                display: flex;
                justify-content: space-between;
                padding: 10px;
                border-bottom: 1px solid #eee;
            }}
            .grade-item:last-child {{
                border-bottom: none;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="welcome-message">Добро пожаловать в Личный кабинет!</div>
                <p>Система для управления учебным процессом</p>
            </div>
            
            <div class="profile-card">
                <h2>Профиль студента</h2>
                <div class="profile-info">
                    <p><strong>ФИО:</strong> {student.first_name} {student.last_name}</p>
                    <p><strong>Email:</strong> {student.email}</p>
                    <p><strong>Группа:</strong> {student.group}</p>
                    <p><strong>ID:</strong> {student.id}</p>
                </div>
            </div>
            
            <div class="grades-card">
                <h2>Успеваемость</h2>
                <div class="grades-list">
    '''
    
    for subject, grade in student.grades.items():
        html += f'''
                    <div class="grade-item">
                        <span>{subject}</span>
                        <span><strong>{grade}</strong></span>
                    </div>
        '''
    
    html += '''
                </div>
            </div>
        </div>
    </body>
    </html>
    '''
    
    return html

if __name__ == '__main__':
    app.run(debug=True)