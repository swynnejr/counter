from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    
    return render_template("index.html")

# @app.route('/destroy_session')
# def counter():
    
#     return redirect("/")





if __name__=="__main__":
    app.run(debug=True)