from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🎓 Система организации курсов и тренингов</h1>
    <h2>Доступные курсы:</h2>
    
    <div style="background: #f0f0f0; padding: 10px; margin: 10px;">
        <h3>Python для начинающих</h3>
        <p><strong>Длительность:</strong> 40 часов</p>
        <p><strong>Цена:</strong> 15 000 ₽</p>
    </div>
    
    <div style="background: #f0f0f0; padding: 10px; margin: 10px;">
        <h3>Веб-разработка</h3>
        <p><strong>Длительность:</strong> 60 часов</p>
        <p><strong>Цена:</strong> 20 000 ₽</p>
    </div>
    
    <div style="background: #f0f0f0; padding: 10px; margin: 10px;">
        <h3>Анализ данных</h3>
        <p><strong>Длительность:</strong> 50 часов</p>
        <p><strong>Цена:</strong> 18 000 ₽</p>
    </div>
    
    <p><strong>Всего курсов:</strong> 3</p>
    <p><em>Для записи на курс свяжитесь с администратором</em></p>
    '''

if __name__ == '__main__':
    app.run(debug=True)