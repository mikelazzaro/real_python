# views.py

import sqlite3
from functools import wraps
from flask import Flask, flash, redirect, render_template, request, \
                    session, url_for, g


app = Flask(__name__)
app.config.from_object('config')


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap



@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('And stay out!')
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
                request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials! Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('tasks'))
    return render_template('login.html', error=error)


@app.route('/tasks/')
@login_required
def tasks():
    g.db = connect_db()
    cur = g.db.execute('SELECT name, due_date, priority, task_id FROM ftasks WHERE status=1')
    open_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cur.fetchall()]
    cur = g.db.execute('SELECT name, due_date, priority, task_id FROM ftasks WHERE status=0')
    closed_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('tasks.html', open_tasks=open_tasks, closed_tasks=closed_tasks)

# Add new tasks
@app.route('/add/', methods=['POST'])
@login_required
def new_task():
    g.db = connect_db()
    name = request.form['name']
    date = request.form['date']
    priority = request.form['priority']
    if not all([name, date, priority]):
        flash("All fields are required!")
        return redirect(url_for('tasks'))
    else:
        g.db.execute('INSERT INTO ftasks (name, due_date, priority, status) VALUES (?, ?, ?, 1))',
                        [request.form[f] for f in ['name', 'date', 'priority']])
        g.db.commit()
        g.db.close()
        flash('New entry successfully posted.')
        return redirect(url_for('tasks'))


# Mark as complete
@app.route('/complete/<int:task_id>/',)
@login_required
def complete(task_id):
    g.db = connect_db()
    cur = g.db.execute('UPDATE ftasks SET status = 0 WHERE task_id = {}'.format(task_id))
    g.db.commit()
    g.db.close()
    flash('Task marked complete.')
    return redirect(url_for('tasks'))

# Delete tasks
@app.route('/delete/<int:task_id>/',)
@login_required
def delete_entry(task_id):
    g.db = connect_db()
    cur = g.db.execute('DELETE FROM ftasks WHERE task_id = {}'.format(task_id))
    g.db.commit()
    g.db.close()
    return redirect(url_for('tasks'))


