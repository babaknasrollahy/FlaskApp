from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def index():
    return render_template('index.html')
     
@app.route('/show/', methods=['POST'])
def show(): 
    HisName = request.form.get('user')
    return f"<h1>Welcome dear {HisName}</h1>"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)