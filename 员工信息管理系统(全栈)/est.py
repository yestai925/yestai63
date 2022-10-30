from flask import Flask, render_template, request
from data import salary_list
# Разработка программы для маркетологов для управления бизнесом
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('est.html')

@app.route('/login', methods=["POST","GET"])
def hello_login():
        #print(request.form)
        username=request.form.get('username')
        password=request.form.get('password')
        print(username ,password)

        #for sal in salary_list:
        #if sal ['name']==username:

        assert isinstance(salary_list, object)
        return render_template('admin.html',salary_list=salary_list)
@app.route('/delete/<name>')
def hello_delete(name):
    for salary in salary_list:
        if salary['name']==name:
            salary_list.remove(salary)
    return render_template('admin.html',
                           salary_list=salary_list)

@app.route('/change/<name>')
def hello_change(name):
    for salary in salary_list:
        if salary['name']==name:
            return render_template('change.html',
                               user=salary)
    return render_template('admin.html',
                           salary_list=salary_list)

@app.route('/changed/<name>',methods=["POST"])
def hello_changed(name):
    for salary in salary_list:
        if salary['name']== name:
            salary['name']=request.form.get('name')
            salary['department'] = request.form.get('department')
            salary['position'] = request.form.get('position')
            salary['salary'] = request.form.get('salary')

    return render_template('admin.html',
                            salary_list=salary_list)

@app.route('/add')
def hello_add():
    return render_template('add.html')

    @app.route('/add2',methods=['POST'])
    def hello_add2():
        salary = {}
    salary['name'] = request.form.get('name')
    salary['department'] = request.form.get('department')
    salary['position'] = request.form.get('position')
    salary['salary'] = request.form.get('salary')
    salary_list.insert(0,salary)
    return render_template('admin.html',
                           salary_list=salary_list)

if __name__ == '__main__':
    app.run( )