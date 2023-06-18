from flask import Flask, send_file

app = Flask(__name__)

@app.route('/random_values', methods=['GET'])
def get_random_values():
    file_path = 'random_values.txt'

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

        return file_content.replace('\n', '<br>')

    except FileNotFoundError:
        return 'Error: File not found'

if __name__ == '__main__':
    app.run()


