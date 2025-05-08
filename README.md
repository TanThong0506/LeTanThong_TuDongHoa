# Hướng dẫn chạy mã nguồn của Dự án Thu thập dữ liệu từ Dân Trí
Đây là dự án Python để thu thập dữ liệu từ trang báo Dân Trí. Dự án bao gồm hai chức năng chính:

Thu thập dữ liệu theo chuyên mục.

Thu thập dữ liệu tìm kiếm theo từ khóa.

Các bài viết sẽ được lưu lại dưới dạng file Excel.
## 1.Cài đặt môi trường
Để chạy được mã nguồn này, bạn cần cài đặt một số thư viện Python. Hãy làm theo các bước sau:

- ** Clone dự án về máy**:
 git clone https://github.com/TanThong0506/LeTanThong-TuDongHoa.git
cd LeTanThong-TuDongHoa

- **Cài đặt các thư viện phụ thuộc**:
- Cài đặt các thư viện cần thiết từ file requirements.txt:
  ```bash
    pip install -r requirements.txt
```

---
## 2.Chạy mã nguồn
1. Chạy scraper theo chuyên mục và từ khóa
Mở file scheduler.py và chạy mã nguồn:
 ```bash
    python scheduler.py
```
## 3Lên lịch tự động thu thập dữ liệu
Trong scheduler.py, chúng ta đã cài đặt lịch để mã chạy mỗi ngày lúc 6h sáng:
```bash
  schedule.every().day.at("06:00").do(job)
```
Cấu hình WebDriver
Để Selenium có thể truy cập trang web, bạn cần chỉ định đường dẫn đến ChromeDriver. Trong scheduler.py, hãy thay đổi đường dẫn đến ChromeDriver của bạn, ví dụ:
```bash
  "E:\LeTanThong_BaiTaplon-084e7e95c48b188822eea5946e829e89822fd6ca\chromedriver-win64\chromedriver.exe"
```
Sau khi chạy file scheduler.py thành công , ta sẽ lưu được 2 file exel nằm ở thư mục output
Chúc các bạn thành công 
''
