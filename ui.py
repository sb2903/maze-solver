import tkinter as tk
from tkinter import simpledialog
from logic import find_paths

# Ask user for size
root = tk.Tk()
root.withdraw()
n = simpledialog.askinteger("Maze Size", "Enter maze size (e.g., 4):", minvalue=2, maxvalue=20)

maze = [[1 for _ in range(n)] for _ in range(n)]

root = tk.Tk()
root.title("Rat in a Maze")
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(main_frame, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
control_frame = tk.Frame(root)
control_frame.pack(pady=5)
status_label = tk.Label(control_frame, text="", font=("Arial", 12))
status_label.pack(side=tk.LEFT)
path = []
cell_width = cell_height = 0

def draw_maze(event=None):
    canvas.delete("all")
    global cell_width, cell_height
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    cell_width = width / n
    cell_height = height / n

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                color = "green"  # Start
            elif i == n - 1 and j == n - 1:
                color = "red"    # End
            else:
                color = "white" if maze[i][j] == 1 else "black"
            canvas.create_rectangle(
                j * cell_width, i * cell_height,
                (j + 1) * cell_width, (i + 1) * cell_height,
                fill=color, outline="gray"
            )

def toggle_cell(event):
    j = int(event.x // cell_width)
    i = int(event.y // cell_height)
    if 0 <= i < n and 0 <= j < n:
        if (i, j) not in [(0, 0), (n-1, n-1)]: 
            maze[i][j] = 0 if maze[i][j] == 1 else 1
            draw_maze()

def animate_path(path_str, step=0, x=0, y=0):
    if step >= len(path_str):
        return
    move = path_str[step]
    if move == "D": x += 1
    elif move == "U": x -= 1
    elif move == "L": y -= 1
    elif move == "R": y += 1

    canvas.create_rectangle(
        y * cell_width, x * cell_height,
        (y + 1) * cell_width, (x + 1) * cell_height,
        fill="skyblue", outline=""
    )

    root.after(300, animate_path, path_str, step + 1, x, y)

status_label = tk.Label(root, text="", font=("Helvetica", 20))
status_label.pack(pady=5)

def solve_maze():
    global path
    path = find_paths(maze)
    draw_maze()
    status_label.config(text="") 

    if path:
        path_length = len(path[0])
        animation_duration = path_length * 300 
        animate_path(path[0])
        root.after(animation_duration, lambda: status_label.config(
            text="Maze Successfully Solved ✅", fg="green"))
    else:
        status_label.config(text="bkl sahi se bana")
        root.after(2000, root.destroy)

solve_button = tk.Button(control_frame, text="Solve", command=solve_maze)
solve_button.pack(side=tk.LEFT, padx=10)

canvas.bind("<Configure>", draw_maze)
canvas.bind("<Button-1>", toggle_cell)

root.mainloop()
