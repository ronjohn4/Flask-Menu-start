from flask import Flask, render_template
from flask_menu import Menu, register_menu


app = Flask(__name__)
Menu(app=app)


@app.route('/page1')
@app.route('/')
@register_menu(app, 'page1', 'Page1', order=0)
def page1():
    return render_template('page1.html')


@app.route('/page2')
@register_menu(app, 'page2', 'Page2', order=2)
def page2():
    return render_template('page2.html')


@app.route('/page3')
@register_menu(app, 'page3', 'Page3', order=1)
def page3():
    return render_template('page3.html')


if __name__ == '__main__':
    app.run(debug=True)
