# 小猿口算乘法自动答题

该项目使用 Python 捕获屏幕截图，识别图像中的数字，并使用鼠标移动在屏幕上绘制结果。它利用了 `pyautogui`、`pytesseract`、`cv2` 和 `numpy` 等库。
## 演示视频
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 需求

- Python 3.x
- `pyautogui`
- `pytesseract`
- `opencv-python`
- `numpy`
- `keyboard`
- `xlrd`
- `pyperclip`
- `matplotlib`

## 安装

1. 克隆仓库：
    ```bash
    git clone https://github.com/Ben1524/screen-drawing.git
    cd screen-drawing
    ```

2. 安装所需的包：
    ```bash
    pip install pyautogui pytesseract opencv-python numpy keyboard xlrd pyperclip matplotlib
    ```

3. 安装 Tesseract OCR：
    - 从[这里](https://github.com/tesseract-ocr/tesseract)下载并安装 Tesseract。
    - 更新脚本中的 `pytesseract.pytesseract.tesseract_cmd` 路径为安装位置。

## 使用
> 注意安卓模拟器的分辨率为 1920x1080，如果不是，请修改 `main.py` 中的 `capture_area` 函数。

> 建议使用windows 的 windows subsystem for Android 模拟器，可以直接使用windows的tesseract-ocr

1. 运行脚本：
    ```bash
    python main.py
    ```

2. 脚本将连续捕获屏幕，识别数字，并在屏幕上绘制结果。

3. 要退出脚本，请按 `=` 键。

## 函数

### `draw_digit(digit, start_x, start_y, scale=1.5)`
在指定坐标处以给定比例绘制单个数字。

### `draw_number(number, start_x, start_y, scale=2)`
通过调用 `draw_digit` 为数字中的每个数字在屏幕上绘制一个数字。

### `capture_area()`
捕获屏幕截图并返回图像。

### `recognize_numbers(image)`
使用 Tesseract OCR 识别给定图像中的数字。

### `draw_comparison(numbers)`
比较识别的数字并在屏幕上绘制结果。

### `main()`
主函数，循环运行脚本，捕获屏幕，识别数字，并绘制结果。

