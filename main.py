import pyautogui
import time
import xlrd
import pyperclip
import matplotlib.pyplot as plt
import re
import cv2
import numpy as np
import pyautogui
import pytesseract
import keyboard
import sys
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

not_found_count = 0
last_not_found_time = 0
last_numbers = None  # 用于存储上次识别的数字
skip_count = 0  # 跳过次数计数器



import pyautogui
import time

def draw_digit(digit, start_x, start_y, scale=1.5):
    # 定义数字的绘制路径
    digits = {
        '0': [(0, 0), (1,0), (0.75, 1),  (0, 1), (0, 0)],
        '1': [(0.5, 0), (0.5, 1)],
        '2': [(0, 1), (1, 1), (0, 0), (1, 0)],
        '3': [(0, 1), (1, 1), (0, 0.5), (1, 0), (0, 0)],
        '4': [(0, 1), (0, 0.5), (1, 0.5), (0.5,0.5),(0.5, 1), (0.5, 0)],
        '5': [(1, 1), (0, 1), (1, 0), (0, 0)],
        '6': [(0, 1), (0, 0), (1, 0), (0, 0.5)],
        '7': [(1, 0), (1, 1), (0, 1)],
        '8': [(1,1), (0, 0), (1, 0), (0, 1), (1, 1)],
        '9': [(1, 0), (1, 1), (0, 0.25),  (1, 0.5)]
    }

    digits2 = {
        '0': [(0, 0.5), (1, 0), (1, 1), (0, 0.5)],
        '1': [(0.5, 0), (0.5, 1)],
        '2': [(0, 1), (1, 1), (0, 0), (1, 0)],
        '3': [(0, 1), (1, 1), (0, 0.5), (1, 0), (0, 0)],
        '4': [(0, 1), (0, 0.5), (1, 0.5), (0.5, 0.5), (0.5, 1), (0.5, 0)],
        '5': [(1, 1), (0, 1), (1, 0), (0, 0)],
        '6': [(0, 1), (0, 0), (1, 0), (0, 0.5)],
        '7': [(0,1), (1, 1), (1, 0)],
        '8': [(1, 1), (0, 0), (1, 0), (0, 1), (1, 1)],
        '9': [(1, 0), (1, 1), (0, 0.25), (1, 0.5)]
    }


    # 获取数字的路径
    path = digits.get(str(digit), [])

    if np.random.randint(0, 2) == 0: # 50%的概率使用另一种路径
        path = digits2.get(str(digit), [])
    if not path:
        print(f"Unsupported digit: {digit}")
        return

    # 将路径转换为屏幕坐标，并应用放大系数
    path = [(start_x + x * 70 * scale, start_y - y * 70 * scale) for x, y in path]


    # 移动到起始位置
    pyautogui.moveTo(path[0][0], path[0][1])

    pyautogui.mouseDown()  # 按下鼠标左键
    # 绘制数字
    for x, y in path[1:]:
        pyautogui.moveTo(x, y)
        time.sleep(0.1)  # 控制绘制速度
        #pyautogui.mouseUp()  # 松开鼠标左键
    # 画最后一笔

    pyautogui.mouseDown()  # 按下鼠标左键
    pyautogui.moveTo(path[-2][0], path[-2][1])
    pyautogui.moveTo(path[-1][0], path[-1][1])


    pyautogui.mouseUp()

def draw_number(number, start_x, start_y, scale=2):
    offset = 0
    pyautogui.moveTo(start_x, start_y)

    for digit in str(number):
        draw_digit(digit, start_x + offset, start_y, scale)
        offset += 150  # 每个数字之间的间隔

# 示例：在屏幕上绘制放大的数字 1500





def capture_area():
    #image = pyautogui.screenshot(region=(0, 0, 1080, 1920))
    # 全屏截图
    image = pyautogui.screenshot()
    #image=cv2.imread("test.png")
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("test.png", image)

    if(image is None):
        print("截图失败")
        return cv2.imread("test2.png")
    #
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用 pytesseract 获取图像中的文本位置
    #boxes = pytesseract.image_to_boxes(gray, output_type=pytesseract.Output.DICT, config='--psm 6')
    boxes = pytesseract.image_to_boxes(gray,  config='--psm 6')
    # 找到乘法表达式的位置
    # for i in range(len(boxes['text'])):
    #     #if boxes['text'][i] == '×':
    #     if 'x' in boxes['text'][i] or 'X' in boxes['text'][i]:
    #         print(boxes['text'][i])
    #
    #         x, y, w, h = boxes['left'][i], boxes['top'][i], boxes['width'][i], boxes['height'][i]
    #         x -= 10
    #         y -= 10
    #         w-=15
    #         h+=20
    #         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #         # 截取保存矩形区域
    #         roi = image[y:y + h, x:x + w]
    #         # Save the ROI to a file
    #
    #         cv2.imwrite("roi.png", roi)
    #
    #         return roi
    #

    for b in boxes.splitlines():
        b = b.split(' ')
        if b[0] == '=':
            print(b)
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            x -= 300
            y -= 50

            h += 50
            cv2.rectangle(image, (x, image.shape[0] - y), (w, image.shape[0] - h), (0, 255, 0), 2)
            # 截取保存矩形区域
            roi = image[image.shape[0] - h:image.shape[0] - y, x:w - 18]

            # Save the ROI to a file

            return roi

    return cv2.imread("test2.png")


def recognize_numbers(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh, config='--psm 6')
    print(text)

    if 'x' not in text and  'X' not in text:
        print("未找到乘法表达式")
        return []


    numbers = [int(s) for s in text.split() if s.isdigit()]
    if len(numbers) < 2:
        print("未找到足够的数字")
        # 47x47
        print("尝试使用自定义模式识别")
        # 正则表达式匹配数字
        numbers = re.findall(r"\d+", text)
        numbers = [int(n) for n in numbers]

    return numbers


def draw_comparison(numbers):
    global not_found_count, last_not_found_time, last_numbers, skip_count

    if len(numbers) < 2:
        current_time = time.time()
        if not_found_count == 0 or current_time - last_not_found_time > 1:
            not_found_count = 1
        else:
            not_found_count += 1

        last_not_found_time = current_time
        print("未找到足够的数字进行比较")

        if not_found_count >= 25:
            pyautogui.click(950, 692)  # 点击“开心收下”按钮
            time.sleep(0.3)
            pyautogui.click(1430, 960)  # 点击“继续”按钮
            time.sleep(0.3)
            pyautogui.click(960, 910)  # 点击“继续PK”按钮
            time.sleep(13)
            print("准备重新开始程序...")
            time.sleep(0.3)
            main()
        return

    if last_numbers is not None and last_numbers == numbers:
        skip_count += 1
        print(f"当前结果与上次相同，跳过此次执行 (次数: {skip_count})")

        if skip_count > 3:  # 超过5次则强制执行一次
            skip_count = 0  # 重置计数器
            print("跳过次数超过5次，强制执行一次")
            # 在这里可以直接执行绘制逻辑，或根据需要处理
            first, second = numbers[0], numbers[1]
            origin_x, origin_y = 250, 650  # 绘制区域坐标
            size = 50
            result = first * second
            # 随机偏移
            rx, ry = np.random.randint(-30, 30, 2)
            # 绘制数字在屏幕上
            draw_number(result, 450 + rx, 800 + ry, 1.2)

        return

    first, second = numbers[0], numbers[1]

    result = first * second
    print(f"{first} * {second} = {result}")

# 随机偏移
    rx, ry = np.random.randint(-30, 30, 2)
    # 绘制数字在屏幕上
    draw_number(result, 450 + rx, 800 + ry, 1.2)



    not_found_count = 0
    last_numbers = numbers  # 更新 last_numbers 为当前数字
    skip_count = 0  # 重置跳过次数

def main():
    keyboard.add_hotkey('=', lambda: sys.exit("进程已结束"))  # 默认退出快捷键是 "="

    try:
        while True:
            image = capture_area()
            numbers = recognize_numbers(image)
            print(numbers)

            draw_comparison(numbers)
            time.sleep(0.29)  # 每次绘制及识别的延迟，有了last_numbers判断现在好像不需要延迟了
    except SystemExit as e:
        print(e)


if __name__ == "__main__":
    main()