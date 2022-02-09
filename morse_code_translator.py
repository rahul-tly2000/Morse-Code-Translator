from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

morse_code = {
    'A' : '·-',
    'B' : '-···',
    'C' : '-·-·',
    'D' : '-··',
    'E' : '·',
    'F' : '··-·',
    'G' : '--·',
    'H' : '····',
    'I' : '··',
    'J' : '·---', 
    'K' : '-·-',
    'L' : '·-··',
    'M' : '--',
    'N' : '-·',
    'O' : '---',
    'P' : '·--·',
    'Q' : '--·-',
    'R' : '·-·',
    'S' : '···',
    'T' : '-',
    'U' : '··-',
    'V' : '···-',
    'W' : '·---',
    'X' : '-··-',
    'Y' : '-·--',
    'Z' : '--··',
    ' ' : '/',
    '!' : '-·-·--',
    ':' : '---···',
    '"' : '·-··-·',
    "'" : "·----·",
    '=' : '-···-',
    '+' : '·-·-·',
    '(' : '-·--·',
    ')' : '-·--·-',
    '&' : '·-···',
    '@' : '·--·-·',
    '/' : '-··-·',
    '.' : '·-·-·-',
    ',' : '--··--',
    '?' : '··--··',
    '1' : '·----',
    '2' : '··---',
    '3' : '···--',
    '4' : '····-',
    '5' : '·····',
    '6' : '-····',
    '7' : '--···',
    '8' : '---··',
    '9' : '----·',
    '0' : '-----'
}


@app.route('/', methods=['GET', 'POST'])
def home():
    code = ''
    message = None
    if request.method == 'POST':
        message= request.form['message']
        message_upper = message.upper()
        for letter in message_upper:
            try:
                tr_letter = morse_code[letter]
            except KeyError:
                tr_letter = '#'
            code += f'{tr_letter} '

        print(code)

    return render_template('morse_code_translator.html', result=code, msg=message)

if __name__ == '__main__':
    app.run(debug=True)