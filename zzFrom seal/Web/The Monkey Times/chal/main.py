
from flask import Flask, render_template, request, send_file
import sqlite3
app = Flask(__name__, template_folder='templates')
 
connection = sqlite3.connect('posts.db')
with open('posts.sql') as f:
    connection.executescript(f.read())
    connection.commit()
    connection.close()
    f.close()

def get_db_connection():
    conn = sqlite3.connect('posts.db')
    conn.row_factory = sqlite3.Row
    return conn
 
 
@app.route('/', methods=['GET'])
def main():
    post_id=request.args.get('id')
    if post_id:
        conn = get_db_connection()
        try:
            if int(post_id) == 3:
                return render_template('index.html', error='You can\'t look at the flag!')
        except:
            print('Not a number!')
        posts = conn.execute('SELECT * FROM posts WHERE id=\''+post_id+'\'').fetchall()
        conn.close()
        return render_template('index.html', posts=posts)
    else:
        return render_template('index.html')

 
if __name__ == '__main__':
    app.run()
