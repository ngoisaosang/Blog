import sqlite3

#Kết nối đến cơ sở dữ liệu SQLite (nếu không tồn tại sẽ tự tạo)
connection =sqlite3.connect('blog.db')

#Đọc và thực thi tệp schema.sql để tạo bảng
with open('schema.sql') as f:
    connection.executescript(f.read())

#Tạo cursor để thực thi các lệnh SQL
cur = connection.cursor()

#Thêm dữ liệu mẫu vào bảng posts
cur.execute("INSERT INTO posts(title,content) VALUES (?, ?)",
            ('Bài viết đầu tiên','Nội dung cho bài viết đầu tiên'))
cur.execute("INSERT INTO posts(title,content) VALUES(?,?)", 
           ('Bài viết thứ hai','Nội dung cho bài viết thứ hai'))

#Lưu các thay đổi và đóng kết nối
connection.commit()
connection.close()
