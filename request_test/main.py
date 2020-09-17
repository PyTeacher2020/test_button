from flask import Flask, render_template
from flask import request
import modul
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cite.html')


@app.route('/process_data/', methods=['POST'])
def doit():
    ans=modul.test_func()
    print(ans)
    return render_template('cite.html')