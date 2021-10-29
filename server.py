from flask import Flask, render_template
from board import make_checkerboard
app = Flask(__name__)

@app.route('/<int:x>/<int:y>/')
def checkerboard(x,y ):
    result = make_checkerboard(x,y)
    return render_template("check.html", result=result)


# @app.route('/<int:num>')
# def play_page(num_w):
#     return render_template("check.html", num_w=num_w, color1="red", color2="black")

# @app.route('/<int:num1>/<int:num2>')
# def boxes_repeat2(num_l, color, color2):
#     return render_template("check.html", num_l=num_l, color=color, color2=color2)

if __name__=="__main__":
    app.run(debug=True) 