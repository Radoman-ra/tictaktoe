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
    window.destroy()


def button_click(event):
    global turn
    if event.cget("text") == "":
        global counter
        counter -= 1
        if counter != 0:
            event.config(text=turn)
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

            # Проверяем горизонталь
            # Проверяем слева
            while left_check < win:
                if col_inf - left_check >= 0:
                    if buttons_list[row_inf][col_inf - left_check] == turn:
                        right_and_left_counter += 1
                        print(right_and_left_counter)
                        left_check += 1
                        if left_check == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
                    else:
                        break
                else:
                    break
            # Проверяем справа + общ
            while right_check < win:
                if col_inf + right_check < grid_size:
                    if buttons_list[row_inf][col_inf + right_check] == turn:
                        right_and_left_counter += 1
                        print(right_and_left_counter)
                        right_check += 1
                        if right_check == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
                        elif right_and_left_counter == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
                    else:
                        break
                else:
                    break

            # Проверяем вертикаль
            # Проверяем сверху
            while up_check < win:
                if row_inf - up_check >= 0:
                    if buttons_list[row_inf - up_check][col_inf] == turn:
                        up_down += 1
                        print(up_down)
                        up_check += 1
                        if up_check == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
                    else:
                        break
                else:
                    break
            # Проверяем снизу + общ
            while down_check < win:
                if row_inf + down_check < grid_size:
                    if buttons_list[row_inf + down_check][col_inf] == turn:
                        up_down += 1
                        print(up_down)
                        down_check += 1
                        if down_check == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
                        elif up_down == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
                    else:
                        break
                else:
                    break

            # Проверяем диагональ
            # Слева сверху
            while left_up_deagonal_check < win:
                if row_inf + left_up_deagonal_check < grid_size and col_inf - left_up_deagonal_check >= 0:
                    if buttons_list[row_inf + left_up_deagonal_check][col_inf - left_up_deagonal_check] == turn:
                        left_up_right_down_deagonal_counter += 1
                        print(left_up_right_down_deagonal_counter)
                        left_up_deagonal_check += 1
                        if left_up_deagonal_check == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
                    else:
                        break
                else:
                    break
            # Справа снизу + общ
            while right_down_deagonal_check < win:
                if row_inf - right_down_deagonal_check >= 0 and col_inf + right_down_deagonal_check < grid_size:
                    if buttons_list[row_inf - right_down_deagonal_check][col_inf + right_down_deagonal_check] == turn:
                        left_up_right_down_deagonal_counter += 1
                        print(left_up_right_down_deagonal_counter)
                        right_down_deagonal_check += 1
                        if right_down_deagonal_check == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
                        elif left_up_right_down_deagonal_counter == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
                    else:
                        break
                else:
                    break

            # Проверяем диагональ
            # Слева снизу
            while left_down_deagonal_check < win:
                if row_inf - left_down_deagonal_check >= 0 and col_inf - left_down_deagonal_check >= 0:
                    if buttons_list[row_inf - left_down_deagonal_check][col_inf - left_down_deagonal_check] == turn:
                        left_down_right_up_deagonal_counter += 1
                        print(left_down_right_up_deagonal_counter)
                        left_down_deagonal_check += 1
                        if left_down_deagonal_check == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
                    else:
                        break
                else:
                    break
            # Справа сверху + общ
            while right_up_deagonal_check < win:
                if row_inf + right_up_deagonal_check < grid_size and col_inf + right_up_deagonal_check < grid_size:
                    if buttons_list[row_inf + right_up_deagonal_check][col_inf + right_up_deagonal_check] == turn:
                        left_down_right_up_deagonal_counter += 1
                        print(left_down_right_up_deagonal_counter)
                        right_up_deagonal_check += 1
                        if right_up_deagonal_check == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
                        elif left_down_right_up_deagonal_counter == win:
                            end_music()
                            messagebox.showinfo("THE END", f"{turn} win!!!!!")
                            restart()
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
            messagebox.showinfo("THE END", f"идите нахуй с такой игрой")
            restart()


def apply_settings():
    try:
        global grid_size, win, buttons_list, counter
        grid_size = int(entry_Grid_size.get())
        win = int(entry_win.get())
        counter = grid_size * grid_size
        print(f"Применены настройки: grid_size={grid_size}, win={win}")
        if win <= grid_size and win > 1 and grid_size > 1:
            global window
            main_music()
            window = Toplevel(menu)
            window.geometry(f'{67 * grid_size}x{67 * grid_size}')
            window.title('Tictaktoe')
            window.configure(bg='black')

            # Инициализация списка кнопок
            buttons_list = []

            for row in range(grid_size):
                buttons_row = []
                for col in range(grid_size):
                    print(row, col)
                    button = tk.Button(
                        window,  # Указываем родительское окно
                        text="",
                        width=int(button_size),
                        height=int(button_size / 2),
                        font=("Arial", 0),
                    )
                    button.grid(column=col, row=row, padx=1, pady=2)
                    button.bind("<Button-1>", lambda event, btn=button: button_click(btn))
                    buttons_row.append(button)  # Добавляем кнопку в текущий ряд
                buttons_list.append(buttons_row)  # Добавляем ряд в список кнопок
        else:
            messagebox.showinfo("ERROR", "WIN is nigger than GRID SIZE")
    except ValueError:
        messagebox.showinfo("ERROR", "Eб твою мать ты никогда не пользовался приложениями?\n \nЗАПОЛНИ ПОЛЯ СУКА")


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

# Поле ввода для параметра win
frame_win = tk.Frame(menu)
frame_win.pack(pady=5)
label_win = tk.Label(frame_win, text="Win:")
label_win.grid(row=0, column=0, padx=5, pady=5)
entry_win = tk.Entry(frame_win, width=10)
entry_win.grid(row=0, column=1, padx=5, pady=5)
button_apply = tk.Button(menu, text="Применить настройки", command=apply_settings)
button_apply.pack(pady=20)
menu.mainloop()
