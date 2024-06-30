import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

import pygame

pygame.init()
turn = "X"
buttons_list = []
menu = tk.Tk()
counter = 0

# ---------------------------------------------------
# best grid size <=20
grid_size = 16
button_size = 5
win = 3
# ---------------------------------------------------

def end_music():
    pygame.mixer.music.load('end.mp3')
    pygame.mixer.music.play()


def error_music():
    pygame.mixer.music.load('eror.mp3')
    pygame.mixer.music.play()


def main_music():
    pygame.mixer.music.load('main_music.mp3')
    pygame.mixer.music.play(-1)


def restart():
    global window
    window.destroy()
    menu.deiconify()
def win_notification():
    end_music()
    messagebox.showinfo("THE END", f"{turn} win!!!!!")
    restart()


def button_click(event):
    global turn
    if event.cget("text") == "":
        global counter
        counter -= 1
        if counter != 0:
            event.config(text=turn)

            if turn == "X":
                event.config(fg="red")
            else:
                event.config(fg="blue")

            info = event.grid_info()
            row_inf = info["row"]
            col_inf = info["column"]
            buttons_list[row_inf][col_inf] = turn
            print(str(row_inf) + " " + str(col_inf))
            right_check = 1
            left_check = 1
            right_and_left_counter = 1

            up_check = 1
            down_check = 1
            up_down = 1

            left_up_deagonal_check = 1
            right_down_deagonal_check = 1
            left_up_right_down_deagonal_counter = 1

            left_down_deagonal_check = 1
            right_up_deagonal_check = 1
            left_down_right_up_deagonal_counter = 1

            # Checking the horizontal
            # Check on the left

            while left_check < win:
                if col_inf - left_check >= 0:
                    if buttons_list[row_inf][col_inf - left_check] == turn:
                        right_and_left_counter += 1
                        print(right_and_left_counter)
                        left_check += 1
                        if left_check == win:
                            win_notification()
                    else:
                        break
                else:
                    break

            # Check on the right + general

            while right_check < win:
                if col_inf + right_check < grid_size:
                    if buttons_list[row_inf][col_inf + right_check] == turn:
                        right_and_left_counter += 1
                        print(right_and_left_counter)
                        right_check += 1
                        if right_check == win:
                            win_notification()
                        elif right_and_left_counter == win:
                            win_notification()
                    else:
                        break
                else:
                    break

            # Checking the vertical
            # We check from above

            while up_check < win:
                if row_inf - up_check >= 0:
                    if buttons_list[row_inf - up_check][col_inf] == turn:
                        up_down += 1
                        print(up_down)
                        up_check += 1
                        if up_check == win:
                            win_notification()
                    else:
                        break
                else:
                    break

            # Check from below + general

            while down_check < win:
                if row_inf + down_check < grid_size:
                    if buttons_list[row_inf + down_check][col_inf] == turn:
                        up_down += 1
                        print(up_down)
                        down_check += 1
                        if down_check == win:
                            win_notification()
                        elif up_down == win:
                            win_notification()
                    else:
                        break
                else:
                    break

            # Checking the diagonal
            # Top left

            while left_up_deagonal_check < win:
                if row_inf + left_up_deagonal_check < grid_size and col_inf - left_up_deagonal_check >= 0:
                    if buttons_list[row_inf + left_up_deagonal_check][col_inf - left_up_deagonal_check] == turn:
                        left_up_right_down_deagonal_counter += 1
                        print(left_up_right_down_deagonal_counter)
                        left_up_deagonal_check += 1
                        if left_up_deagonal_check == win:
                            win_notification()
                    else:
                        break
                else:
                    break

            # Bottom right + general

            while right_down_deagonal_check < win:
                if row_inf - right_down_deagonal_check >= 0 and col_inf + right_down_deagonal_check < grid_size:
                    if buttons_list[row_inf - right_down_deagonal_check][col_inf + right_down_deagonal_check] == turn:
                        left_up_right_down_deagonal_counter += 1
                        print(left_up_right_down_deagonal_counter)
                        right_down_deagonal_check += 1
                        if right_down_deagonal_check == win:
                            win_notification()
                        elif left_up_right_down_deagonal_counter == win:
                            win_notification()
                    else:
                        break
                else:
                    break

            # Checking the diagonal
            # Bottom left

            while left_down_deagonal_check < win:
                if row_inf - left_down_deagonal_check >= 0 and col_inf - left_down_deagonal_check >= 0:
                    if buttons_list[row_inf - left_down_deagonal_check][col_inf - left_down_deagonal_check] == turn:
                        left_down_right_up_deagonal_counter += 1
                        print(left_down_right_up_deagonal_counter)
                        left_down_deagonal_check += 1
                        if left_down_deagonal_check == win:
                            win_notification()
                    else:
                        break
                else:
                    break

            # Top right + general

            while right_up_deagonal_check < win:
                if row_inf + right_up_deagonal_check < grid_size and col_inf + right_up_deagonal_check < grid_size:
                    if buttons_list[row_inf + right_up_deagonal_check][col_inf + right_up_deagonal_check] == turn:
                        left_down_right_up_deagonal_counter += 1
                        print(left_down_right_up_deagonal_counter)
                        right_up_deagonal_check += 1
                        if right_up_deagonal_check == win:
                            win_notification()
                        elif left_down_right_up_deagonal_counter == win:
                            win_notification()
                    else:
                        break
                else:
                    break

            if turn == "X":
                turn = "O"
            else:
                turn = "X"
        else:
            error_music()
            messagebox.showinfo("THE END", f"The game ended in a draw")
            restart()


def apply_settings():
    try:
        global grid_size, win, buttons_list, counter
        grid_size = int(entry_Grid_size.get())
        win = int(entry_win.get())
        counter = grid_size * grid_size
        print(f"Settings applied: grid_size={grid_size}, win={win}")
        if win <= grid_size and win > 1 and grid_size > 1:
            global window
            main_music()
            window = Toplevel(menu)
            window.geometry(f'{67 * grid_size}x{67 * grid_size}')
            window.title('Tictaktoe')
            window.configure(bg='black')

            buttons_list = []
            for row in range(grid_size):
                buttons_row = []
                for col in range(grid_size):
                    print(row, col)
                    button = tk.Button(
                        window,
                        text="",
                        width=int(button_size),
                        height=int(button_size / 2),
                        font=("Arial", 0),
                    )
                    button.grid(column=col, row=row, padx=1, pady=2)
                    button.bind("<Button-1>", lambda event, btn=button: button_click(btn))
                    buttons_row.append(button)
                buttons_list.append(buttons_row)

            menu.withdraw()
        else:
            error_music()
            messagebox.showinfo("ERROR", "WIN is greater than GRID SIZE")
    except ValueError:
        error_music()
        messagebox.showinfo("ERROR", "Please enter valid numbers for Grid Size and Win conditions")


# -----------------
# MENU
# -----------------

menu.geometry('200x200')
menu.title('TicTacToe Menu')
label_menu = tk.Label(menu, text="MENU", font=("Arial", 16))
label_menu.pack(pady=10)
frame_Grid_size = tk.Frame(menu)
frame_Grid_size.pack(pady=5)
label_Grid_size = tk.Label(frame_Grid_size, text="Grid size:")
label_Grid_size.grid(row=0, column=0, padx=5, pady=5)
entry_Grid_size = tk.Entry(frame_Grid_size, width=10)
entry_Grid_size.grid(row=0, column=1, padx=5, pady=5)

frame_win = tk.Frame(menu)
frame_win.pack(pady=5)
label_win = tk.Label(frame_win, text="Win:")
label_win.grid(row=0, column=0, padx=5, pady=5)
entry_win = tk.Entry(frame_win, width=10)
entry_win.grid(row=0, column=1, padx=5, pady=5)
button_apply = tk.Button(menu, text="Apply Settings", command=apply_settings)
button_apply.pack(pady=20)
menu.mainloop()
