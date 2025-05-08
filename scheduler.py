import schedule
import time
from datetime import datetime
from scraper import scrape_category, scrape_search

def job():
    now = datetime.now().strftime('%Y-%m-%d')
    category_url = "https://dantri.com.vn/cong-nghe.htm"
    category_filename = f'dantri_category_{now}.xlsx'
    scrape_category(category_url, category_filename)

    keyword = "trí tuệ nhân tạo" 
    search_filename = f'dantri_search_{keyword.replace(" ", "_")}_{now}.xlsx'
    scrape_search(keyword, search_filename)

schedule.every().day.at("02:23").do(job)

print("Đang chạy scheduler... Nhấn Ctrl+C để thoát.")
while True:
    schedule.run_pending()
    time.sleep(60)
