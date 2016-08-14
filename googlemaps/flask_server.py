from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return 'Well Done Boy'

@app.route('/foo', methods = ['GET', 'POST'])
def foo():
	return render_template('maps.html')

if __name__ == '__main__':
	app.run(debug = True)
