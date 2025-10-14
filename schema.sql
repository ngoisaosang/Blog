-- Xoá bảng posts nếu nó đã tồn tại
DROP TABLE IF EXISTS posts;

--Tạo bảng posts
CREATE TABLE posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)