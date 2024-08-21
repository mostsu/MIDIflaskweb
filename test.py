import Adafruit_NeoPixel
import flask
import time

# กำหนดค่า GPIO pin สำหรับไฟ LED Strip
LED_PIN = 18

# กำหนดค่าจำนวนดวงไฟ LED
LED_COUNT = 40

# กำหนดค่า Default IP address สำหรับ Web server
DEFAULT_IP = "0.0.0.0"

# สร้าง object NeoPixel
strip = Adafruit_NeoPixel.NeoPixel(LED_COUNT, LED_PIN, Adafruit_NeoPixel.COLORORDER_RGB)

# ฟังก์ชันสำหรับแสดงสีบนไฟ LED Strip
def show_color(color, num_leds):
    # ตั้งค่าความสว่าง
    strip.brightness = 100

    # ตั้งค่าสี
    for i in range(num_leds):
        strip.setPixelColor(i, color)

    # แสดงสี
    strip.show()

# ฟังก์ชันสำหรับปิดไฟ LED Strip
def turn_off_leds():
    # ตั้งค่าความสว่างเป็น 0
    strip.brightness = 0

    # แสดงสี
    strip.show()

# เริ่มต้น Flask app
app = flask.Flask(__name__)

# กำหนดค่าหน้าจอ HTML
@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>LED Strip Control</title>
</head>
<body>
    <h1>ควบคุมไฟ LED Strip</h1>
    <form method="post">
        <label for="color_picker">เลือกสี:</label>
        <input type="color" id="color_picker" name="color" value="#ffffff"> <br><br>
        <label for="num_leds">จำนวนดวงไฟ:</label>
        <input type="number" id="num_leds" name="num_leds" value="40"> <br><br>
        <input type="submit" value="OK">
        <input type="button" value="ปิดไฟ" onclick="location.href='/turn_off_leds'">
    </form>
</body>
</html>
    """

# ฟังก์ชันสำหรับรับค่าสีและจำนวนดวงไฟจากผู้ใช้
@app.route("/", methods=["POST"])
def change_color():
    color = flask.request.form["color"]
    num_leds = int(flask.request.form["num_leds"])

    # แปลงค่าสีจาก HEX เป็น RGB
    r, g, b = color[1:].split(",")
    rgb_color = (int(r), int(g), int(b))

    # แสดงสีบนไฟ LED Strip
    show_color(rgb_color, num_leds)

    return flask.redirect("/")

# ฟังก์ชันสำหรับปิดไฟ LED Strip
@app.route("/turn_off_leds")
def turn_off_leds():
    turn_off_leds()

    return flask.redirect("/")

# ตั้งค่า Default IP address สำหรับ Web server
if __name__ == "__main__":
    app.run(host=DEFAULT_IP)
