from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime   


app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db= SQLAlchemy(app)


class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())



    def __repr__(self):
        return f"Task {self.id}"

with app.app_context():
    db.create_all()

@app.route('/',methods=['POST','GET'])
def index():
    #Add a task 
    if request.method == 'POST':
        current_task = request.form.get('content')
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f'Error occurred: {e}')
            return f"Error occurred: {e}"
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template("index.html", tasks=tasks)


# Delete an Item
@app.route('/delete/<int:id>')
def delete_task(id: int):
    task_to_delete = MyTask.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f'Error occurred: {e}')
        return f"Error occurred: {e}"


# Edit a Task
# Edit a Task
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id: int):
    task = MyTask.query.get_or_404(id)

    if request.method == 'POST':
        new_content = request.form.get('content')
        if not new_content or new_content.strip() == "":
            return "Error: Task content cannot be empty!"
        
        task.content = new_content
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f'Error occurred: {e}')
            return f"Error occurred: {e}"

    else:
        return render_template("edit.html", task=task)


if __name__ == '__main__':
    app.run(debug=True)
