import tkinter as tk
import math
import time

root = tk.Tk()
root.title("Bunga Simetris 🌻")
root.geometry("600x700")
root.resizable(False, False)

canvas = tk.Canvas(root, width=600, height=700, bg="white")
canvas.pack()

cx, cy = 300, 280
petal_count = 6
petal_length = 150
petal_width = 60

def gambar_bunga():
    # --- Kelopak berbentuk polygon, diarahkan keluar ---
    for i in range(petal_count):
        angle = 2 * math.pi * i / petal_count

        # Titik awal dan akhir arah kelopak
        x1 = cx + 60 * math.cos(angle)
        y1 = cy + 60 * math.sin(angle)
        x2 = cx + (60 + petal_length) * math.cos(angle)
        y2 = cy + (60 + petal_length) * math.sin(angle)

        # Hitung orientasi lebar kelopak (tegak lurus arah utama)
        perp_angle = angle + math.pi / 2
        dx = (petal_width / 2) * math.cos(perp_angle)
        dy = (petal_width / 2) * math.sin(perp_angle)

        # 4 titik ujung kelopak
        points = [
            x1 - dx, y1 - dy,
            x2 - dx, y2 - dy,
            x2 + dx, y2 + dy,
            x1 + dx, y1 + dy
        ]

        canvas.create_polygon(points, fill="#FFD700", outline="#E6A800")
        canvas.update()
        time.sleep(0.25)

    # --- Tengah bunga ---
    canvas.create_oval(
        cx - 80, cy - 80,
        cx + 80, cy + 80,
        fill="#8B4513", outline="#5C3317"
    )
    canvas.update()
    time.sleep(0.3)

    # --- Mata ---
    canvas.create_oval(cx - 25, cy - 20, cx - 10, cy - 5, fill="black")
    canvas.create_oval(cx + 10, cy - 20, cx + 25, cy - 5, fill="black")
    canvas.update()
    time.sleep(0.2)

    # --- Senyum ---
    canvas.create_arc(
        cx - 30, cy, cx + 30, cy + 30,
        start=200, extent=140, style=tk.ARC, outline="black", width=3
    )
    canvas.update()
    time.sleep(0.4)

    # --- Batang ---
    batang_top_y = cy + 80
    batang_bottom_y = 650
    canvas.create_rectangle(cx - 15, batang_top_y, cx + 15, batang_bottom_y, fill="#228B22", outline="#196619")
    canvas.update()
    time.sleep(0.3)

    # --- Daun kiri ---
    canvas.create_oval(cx - 130, cy + 250, cx - 20, cy + 310, fill="#2E8B57", outline="#196619")
    canvas.update()
    time.sleep(0.2)

    # --- Daun kanan ---
    canvas.create_oval(cx + 20, cy + 250, cx + 130, cy + 310, fill="#2E8B57", outline="#196619")
    canvas.update()

# Jalankan animasi setelah 0.5 detik
root.after(500, gambar_bunga)
root.mainloop()