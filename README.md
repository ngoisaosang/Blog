Blog Đơn Giản với Flask và SQLite
Đây là một dự án blog nhỏ được xây dựng bằng Python với framework Flask và cơ sở dữ liệu SQLite. Ứng dụng cho phép người dùng xem danh sách các bài viết, xem chi tiết từng bài, và quản trị viên có thể thực hiện các thao tác CRUD (Tạo, Đọc, Cập nhật, Xóa) trên các bài viết.

✨ Các tính năng chính
Hiển thị danh sách tất cả các bài viết trên trang chủ.

Xem nội dung chi tiết của từng bài viết.

Thêm một bài viết mới với tiêu đề và nội dung.

Chỉnh sửa một bài viết đã tồn tại.

Xóa một bài viết khỏi cơ sở dữ liệu.

Hiển thị thông báo (flash messages) sau khi thực hiện các hành động.

🛠️ Công nghệ sử dụng
Backend: Python 3, Flask

Cơ sở dữ liệu: SQLite 3

Frontend: HTML5, CSS3

🚀 Hướng dẫn cài đặt và chạy chương trình
Làm theo các bước dưới đây để chạy dự án trên máy tính của bạn.

1. Yêu cầu cần có
Python 3.6+ đã được cài đặt.

pip (trình quản lý gói của Python).

2. Tải mã nguồn
Sao chép (clone) repository này về máy của bạn:

git clone <URL_CỦA_REPOSITORY_BẠN>
cd <TÊN_THƯ_MỤC_DỰ_ÁN>

3. Cài đặt thư viện
Cài đặt Flask, là thư viện duy nhất cần thiết cho dự án này:

pip install Flask

4. Khởi tạo Cơ sở dữ liệu
Chạy kịch bản database.py để tạo tệp cơ sở dữ liệu blog.db và thêm vào một vài bài viết mẫu. Lưu ý: Lệnh này chỉ cần chạy một lần duy nhất.

python database.py

Sau khi chạy lệnh này, bạn sẽ thấy một tệp mới có tên blog.db xuất hiện trong thư mục gốc của dự án.

5. Chạy ứng dụng
Khởi động máy chủ phát triển của Flask bằng lệnh sau:

python app.py

Bạn sẽ thấy một thông báo tương tự như sau trong terminal:

 * Serving Flask app 'app'
 * Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)

6. Truy cập trang web
Mở trình duyệt web của bạn và truy cập vào địa chỉ http://127.0.0.1:5000 để xem ứng dụng hoạt động.
