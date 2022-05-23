from bs4 import BeautifulSoup
import requests

r = requests.get("https://network.mobile.rakuten.co.jp/product/smartphone/rakuten-hand/")
c = r.content

soup = BeautifulSoup(c, "html.parser")
category = soup.find_all('div',{'class': 'product-detail-Layout_Btn-modal'})
stock = category.text

def main():
    send_line_notify(stock)

def send_line_notify(notification_message):
    line_notify_token = 'LINEのトークン'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

if ("現在入荷待ち" != stock):
    print("入荷したみたい")
    if __name__ == "__main__":
        main()
else:
    print("入荷待ち")