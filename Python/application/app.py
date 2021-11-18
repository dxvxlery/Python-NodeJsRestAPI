from flask import Flask, jsonify, request

app = Flask(__name__)

from todos import todolist

# Получение данный(Get запрос)
@app.route('/todos')
def getProducts():
    return jsonify({'products': todolist})
@app.route('/products/<string:product_name>')
def getProduct(todo_name):
    todosFound = [
        todo for todo in todolist if todo['name'] == todo_name.lower()]
    if (len(todosFound) > 0):
        return jsonify({'product': todosFound[0]})
    return jsonify({'message': 'Product Not found'})

# Добавление записей в список todolist
@app.route('/todos', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
    }
    todolist.append(new_product)
    return jsonify({'products': todolist})

# Обновление записей в списке todos по его названию
@app.route('/todos/<string:todo_name>', methods=['PUT'])
def editProduct(todo_name):
    todosFound = [todo for todo in todolist if todo['name'] == todo_name]
    if (len(todosFound) > 0):
        todosFound[0]['name'] = request.json['name']
        todosFound[0]['price'] = request.json['price']
       
        return jsonify({
            'message': 'Product Updated',
            'product': todosFound[0]
        })
    return jsonify({'message': 'Product Not found'})

# Удаление записей в списке todos по его названию
@app.route('/todos/<string:todo_name>', methods=['DELETE'])
def deleteTodo(todo_name):
    todosFound = [todo for todo in todolist if todo['name'] == todo_name]
    if len(todosFound) > 0:
        todolist.remove(todosFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': todolist
        })

# Сервер запущен на порте 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)