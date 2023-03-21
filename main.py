from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/', methods=['POST'])
def save_suggestion():
  if 'dontsubmit' in request.form:
    return render_template('love.html')
  remarks = request.form['remarks']
  with open('remarks.txt', 'a') as f:
    f.write(remarks + '\n')
  return render_template('thankyou.html', remarks = remarks)

@app.route('/thankyou')
def thank_you():
  return render_template('thankyou.html')


@app.route('/love')
def love():
  return render_template('love.html')



app.run(host='0.0.0.0', port=81)
