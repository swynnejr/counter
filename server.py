from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def counter():
    
    return render_template("index.html", times = times)

@app.route('/destroy_session')
def counter():
    
    return redirect("/")





if __name__=="__main__":
    app.run(debug=True)