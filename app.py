from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/workers')
def workers():

    headers = ['Фамилия и имя сотрудника', 'Должность сотрудника']

    tableData = [
        {'fruit': 'Дмитрий Нагиев', 'price': 'Хозяин ресторана'},
        {'fruit': 'Виктория Гончарова', 'price': 'Управляющая'},
        {'fruit':'Райан Гослинг', 'price':'Шеф-повар'},
        {'fruit':'Брэд Питт', 'price':'Су-шеф'},
        {'fruit':'Луи Бенуа', 'price':'Повар-кондитер'},
        {'fruit':'Максим Лавров', 'price':'Повар'},
        {'fruit':'Арсений Чуганин', 'price':'Повар'},
        {'fruit':'Фёдор Юрченко', 'price':'Повар'},
        {'fruit':'Екатерина Семёнова', 'price':'Повар молекулярной кухни'},
        {'fruit':'Константин Анисимов', 'price':'Бармен-бариста'}
    ]

    return render_template(
        'workers.html',
        headers=headers,
        tableData=tableData)


@app.route('/menu')
def menu():
    return render_template("menu.html")


@app.route('/management_analysis')
def management_analysis():
    return render_template("management_analysis.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True)
