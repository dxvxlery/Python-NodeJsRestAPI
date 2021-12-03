from flask import Flask, jsonify, request

app = Flask(__name__)

from todos import todolist

# Получение данный(Get запрос)
@app.route('/todos')
def getTodos():
    return jsonify({'todos': todolist})


@app.route('/todos/<string:todo_name>')
def getProduct(todo_name):
    todosFound = [
        todo for todo in todolist if todo['name'] == todo_name]
    if (len(todosFound) > 0):
        return jsonify({'todos': todosFound[0]})
    return jsonify({'message': 'Todos Not found'})



# Добавление записей в список todolist
@app.route('/todos', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'todo': request.json['todo'],
    }
    todolist.append(new_product)
    return jsonify({'todos': todolist})



# Обновление записей в списке todos по его названию
@app.route('/todos/<string:todo_name>', methods=['PUT'])
def editProduct(todo_name):
    todosFound = [todo for todo in todolist if todo['name'] == todo_name]
    if (len(todosFound) > 0):
        todosFound[0]['name'] = request.json['name']
        todosFound[0]['todo'] = request.json['todo']
       
        return jsonify({
            'message': 'Todos Updated',
            'todo': todosFound[0]
        })
    return jsonify({'message': 'Todos Not found'})



# Удаление записей в списке todos по его названию
@app.route('/todos/<string:todo_name>', methods=['DELETE'])
def deleteTodo(todo_name):
    todosFound = [todo for todo in todolist if todo['name'] == todo_name]
    if len(todosFound) > 0:
        todolist.remove(todosFound[0])
        return jsonify({
            'message': 'Todo Deleted',
            'todo': todolist
        })

# Сервер запущен на порте 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
