import sqlite3
import secrets
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

# Hàm để kết nối đến cơ sở dữ liệu
def get_db_connection():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn

# Hàm để lấy bài viết theo ID
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
    
# Khởi tạo ứng dụng Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

# Route cho trang chủ
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY created DESC').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

# Route để xem chi tiết một bài viết
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

# Route để tạo bài viết mới
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Tiêu đề là bắt buộc!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

# Route để chỉnh sửa bài viết
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Tiêu đề là bắt buộc!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

# Route để xóa bài viết
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" đã được xóa thành công!'.format(post['title']))
    return redirect(url_for('index'))

# Chạy ứng dụng
if __name__ == '__main__':
    app.run(debug=True)


