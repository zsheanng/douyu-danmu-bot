from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import random
import time

def get_danmu_list():
    with open("danmu.json", "r", encoding="utf-8") as f:
        return json.load(f)

def run():
    danmu_arr = get_danmu_list()
    current_index = 0

    # 调用本地Edge浏览器
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    live_url = "https://www.douyu.com/1667826?dyshid=3a8dd48-d93c91321fe5fb73d73526aa00021701"
    driver.get(live_url)

    print("页面加载完成，请手动扫码登录，登录完按回车继续")
    input()

    while True:
        send_text = danmu_arr[current_index]
        print(f"即将发送：{send_text}")
        try:
            # 定位斗鱼聊天输入框
            input_box = driver.find_element(By.CLASS_NAME, "ChatSend-txt")
            send_btn = driver.find_element(By.CLASS_NAME, "ChatSend-button")

            # 激活输入框、清空、输入文字
            input_box.click()
            input_box.send_keys(Keys.CONTROL + "a")
            input_box.send_keys(Keys.BACKSPACE)
            input_box.send_keys(send_text)

            # 点击发送
            send_btn.click()

            current_index += 1
            if current_index >= len(danmu_arr):
                current_index = 0
        except Exception as e:
            print(f"发送失败：{e}")

        sleep_sec = random.uniform(20, 30)
        print(f"等待{round(sleep_sec,1)}秒\n")
        time.sleep(sleep_sec)

if __name__ == "__main__":
    run()