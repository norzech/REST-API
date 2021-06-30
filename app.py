from flask import Flask, request
import json
from flask_restful import abort


class Words():
    def __init__(self):
        words = [
            {'id': 1, 'word': 'dog'},
            {'id': 2, 'word': 'cat'},
            {'id': 3, 'word': 'table'},
            {'id': 4, 'word': 'fork'},
            {'id': 5, 'word': 'dog'}
        ]
        self.wordsJ = json.dumps(words)

    def words(self):
        return self.wordsJ

    def is_id(self, id):
        wordsData = json.loads(self.wordsJ)
        for word in wordsData:
            if word['id'] == id:
                return True
        return False

    def create_word(self, task):
        wordsData = json.loads(self.wordsJ)
        if self.is_id(task['id']):
            return "id is taken", 404
        wordsData.append(task)
        self.wordsJ = json.dumps(wordsData)
        return self.wordsJ

    def update_word(self, r_task):
        wordsData = json.loads(self.wordsJ)
        if not self.is_id(r_task['id']):
            return "id not found", 404
        for word in wordsData:
            if int(word["id"]) == r_task['id']:
                word.update(r_task)
                return json.dumps(wordsData)

    def delete_word(self, id):
        wordsData = json.loads(self.wordsJ)
        if not self.is_id(id):
            return 'id not found', 404
        for word in wordsData:
            if int(word["id"]) == id:
                wordsData.remove(word)
                self.wordsJ = json.dumps(wordsData)
                return json.dumps(wordsData)

    def show_unic(self):
        wordsData = json.loads(self.wordsJ)
        word_list = []
        for word in wordsData:
            if word["word"] not in word_list:
                word_list.append(word["word"])
        return json.dumps(word_list)

    def count(self):
        wordsData = json.loads(self.wordsJ)
        key_list = json.loads(show_unic())
        counter = {key:0 for key in key_list}
        for word in wordsData:
            counter[word["word"]] += 1
        return counter


app = Flask(__name__)
w = Words()


@app.route('/')
def home():
    return "hello"


@app.route('/api/words')
def words():
    return w.words()


@app.route('/api/word', methods=['POST'])
def create_word_p():
    request_data = request.get_json()
    word_to_create = request_data["word"]
    return w.create_word(word_to_create)


@app.route('/api/word', methods=['PUT'])
def update_word():
    request_data = request.get_json()
    word_to_update = request_data['word']
    return w.update_word(word_to_update)


@app.route('/api/word/<int:id>', methods=['DELETE'])
def delete_word(id):
    return w.delete_word(id)


@app.route('/api/word/unic')
def show_unic():
    return w.show_unic()


@app.route('/api/word/count')
def count():
    return w.count()


app.run()
