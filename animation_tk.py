import time
import math
from tkinter import *

window = Tk()
land_color = "#8B4513"


window.title("tides")
window.geometry("1200x720")


canvas = Canvas(window, width=1200, height=720)
canvas.pack()


sea = canvas.create_rectangle(0, 600, 1200, 720, fill='blue')
land = canvas.create_polygon(1100,500, 1200, 500, 1200, 720, 300, 820, fill=land_color)
moon = canvas.create_oval(560, 20, 640, 100, fill='grey')
earth = canvas.create_oval(500, 200, 700, 400, fill='turquoise')
line_length = 150
line_angle = 0
x1 = 600
y1 = 300
x2 = 600 + line_length*math.cos(line_angle)
y2 = 300 + line_length*math.sin(line_angle)
line = canvas.create_line(x1, y1, x2, y2, fill="green", width=5)



def move():
    lock = 0
    global line_angle
    text_id = None
    while True:
        # Calculate the sea level based on the line_angle
        sea_level = 30 * abs(math.sin(line_angle))

        # Move sea to the calculated level
        canvas.coords(sea, 0, 600 - sea_level, 1200, 720)

        # Update line_angle and coordinates
        x2 = 600 + line_length * math.cos(line_angle)
        y2 = 300 + line_length * math.sin(line_angle)
        canvas.coords(line, x1, y1, x2, y2)

        # Check if sea_level is at its highest or lowest point
        if sea_level >= 30:
            if text_id is not None:
                canvas.delete(text_id)
            text_id = canvas.create_text(600, 660, text="High Tide", fill="white", font=("Arial", 20))
            window.update()
            time.sleep(2)
            lock = 0


        if sea_level <= 0.4 and lock == 0:
            if text_id is not None:
                canvas.delete(text_id)
            text_id = canvas.create_text(600, 660, text="low Tide", fill="white", font=("Arial", 20))
            window.update()
            time.sleep(2)
            lock = 1

        # Remove the text
        if text_id is not None:
            canvas.delete(text_id)
            text_id = None

        line_angle += math.pi / 180  # rotate line by 1 degree

        # Reset line_angle to 0 when it reaches 360 degrees
        if line_angle >= 2 * math.pi:
            line_angle = 0

        window.update()
        window.after(50)



# start the animation by pressing space
window.bind("<space>", lambda e: move())
window.resizable(height=None, width=None)
window.mainloop()


