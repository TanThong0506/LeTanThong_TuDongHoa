import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    service = Service("E:\LeTanThong_BaiTaplon-084e7e95c48b188822eea5946e829e89822fd6ca\chromedriver-win64\chromedriver.exe")
    return webdriver.Chrome(service=service, options=chrome_options)

def scrape_detail_page(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        content_div = soup.select_one('.singular-content')
        return content_div.get_text(separator='\n', strip=True) if content_div else ''
    except Exception as e:
        print(f"Lỗi khi lấy nội dung từ {url}: {e}")
        return ''

def save_to_excel(data, filename):
    os.makedirs('output', exist_ok=True)
    filepath = os.path.join('output', filename)
    df = pd.DataFrame(data)
    df.to_excel(filepath, index=False)
    print(f"Đã lưu file Excel tại: {filepath}")

def scrape_category(url, output_file='dantri_Timkiem.xlsx', max_pages=3):
    driver = setup_driver()
    articles = []

    for page in range(1, max_pages + 1):
        page_url = url.replace('.htm', f'/trang-{page}.htm') if page > 1 else url
        print(f"🔍 Đang lấy trang: {page_url}")
        driver.get(page_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        items = soup.select('.article-item')

        for item in items:
            title_tag = item.select_one('h3 a')
            link = title_tag['href'] if title_tag else ''
            title = title_tag.get_text(strip=True) if title_tag else ''
            description = item.select_one('.article-excerpt').get_text(strip=True) if item.select_one('.article-excerpt') else ''
            image_tag = item.select_one('img')
            image = image_tag['data-src'] if image_tag and 'data-src' in image_tag.attrs else ''
            content = scrape_detail_page(link)

            articles.append({
                'Tiêu đề': title,
                'Mô tả': description,
                'Hình ảnh': image,
                'Nội dung': content,
                'Link': link
            })

    driver.quit()
    save_to_excel(articles, output_file)


def scrape_search(keyword, output_file='dantri_search.xlsx', max_pages=3):
    keyword_encoded = urllib.parse.quote_plus(keyword)
    articles = []

    for page in range(1, max_pages + 1):
        url = f"https://dantri.com.vn/tim-kiem/{keyword_encoded}.htm?page={page}"
        print(f"Đang tìm kiếm trang: {url}")

        try:
            res = requests.get(url)
            res.raise_for_status()

            if res.status_code == 200:
                print(f"Trang {page} tải thành công.")
                soup = BeautifulSoup(res.text, 'html.parser')
                items = soup.select('.article-item')

                if not items:
                    print(f"Không tìm thấy bài viết nào trên trang {page}, dừng lại.")
                    break  

                for item in items:
                    title_tag = item.select_one('h3 a')
                    link = title_tag['href'] if title_tag else ''
                    title = title_tag.get_text(strip=True) if title_tag else ''
                    description = item.select_one('.article-excerpt').get_text(strip=True) if item.select_one('.article-excerpt') else ''
                    image_tag = item.select_one('img')
                    image = image_tag['data-src'] if image_tag and 'data-src' in image_tag.attrs else ''
                    content = scrape_detail_page(link)

                    articles.append({
                        'Tiêu đề': title,
                        'Mô tả': description,
                        'Hình ảnh': image,
                        'Nội dung': content,
                        'Link': link
                    })
            else:
                print(f"Lỗi {res.status_code} khi tải trang tìm kiếm.")
        
        except requests.exceptions.HTTPError as err:
            print(f"Yêu cầu HTTP thất bại: {err}")
        except Exception as e:
            print(f"Lỗi khác: {e}")

    save_to_excel(articles, output_file)
