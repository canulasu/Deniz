import tkinter as tk
from tkinter import messagebox
import platform
import os

# define key variables

mode = 'light'

# define functions

class menu_functions():

    def about_text():
        messagebox.showinfo('About', 'Deniz Çimen Text Editor V.0.0.1')

def delete_file(event=None): 
    filename = save_query_box.get('1.0', tk.END).strip()
    try:
        os.remove(filename)
        load_text_to_entry()

    except FileNotFoundError:
        messagebox.showinfo('Error', 'File not found!')

def save_text(event=None):

    filename = save_query_box.get('1.0', tk.END).strip()
    text = main_text_box.get('1.0', tk.END)

    with open(f'{filename}', 'a') as file:
        pass

    with open(f'{filename}', 'w') as file:
        pass

    with open(f'{filename}', 'a') as file:
        file.write(text)
    
    messagebox.showinfo('Save', 'File saved successfully!')

def load_text_to_entry():

    messagebox.showinfo('Refresh', 'You will lose any unsaved progress!')

    main_text_box.delete('1.0', tk.END)
        
    filename = save_query_box.get('1.0', tk.END).strip()
    try:
        with open(f'{filename}', 'r') as file:
            text = file.read()
            main_text_box.insert('1.0', text)
    except FileNotFoundError:
        pass

def load_menu():

    menu = tk.Tk()
    menu.title('Menu')
    menu.geometry('200x200')

    about_button = tk.Button(menu, text='About', command=menu_functions.about_text)
    about_button.pack(pady=10, padx=10)

    color_button = tk.Button(menu, text='Change Color', command=change_color_profile)
    color_button.pack(pady=10, padx=10)

    menu.mainloop()

def change_color_profile():

    global mode
    global main_text_box
    global save_query_box

    if mode == 'light':
        main_text_box.configure(bg='black')
        main_text_box.configure(fg='white')
        save_query_box.configure(bg='black')
        save_query_box.configure(fg='white')
        mode = 'dark'

    elif mode == 'dark':
        main_text_box.configure(bg='white')
        main_text_box.configure(fg='black')
        save_query_box.configure(bg='white')
        save_query_box.configure(fg='black')
        mode = 'light'

root = tk.Tk()

root.title('Çimen Text Editor')
root.attributes('-fullscreen', True)

top_frame = tk.Frame(root)
top_frame.pack(side='top', anchor='nw', pady=10, padx=10, fill='x')

save_button = tk.Button(top_frame, text='Save', command=save_text)
save_button.pack(side='left', padx=10)

refresh_button = tk.Button(top_frame, text='Refresh', command=load_text_to_entry)
refresh_button.pack(side='left', padx=10)

menu_button = tk.Button(top_frame, text='Menu', command=load_menu)
menu_button.pack(side='left', padx=10)

save_query_box = tk.Text(top_frame, width=40, height=1)
save_query_box.pack(side='right', padx=10)

main_text_box = tk.Text(root, width=40, height=20)
main_text_box.pack(pady=10, padx=10, expand=True, fill='both')

if platform.system() == 'Darwin':
    root.bind('<Command-s>', save_text)
    root.bind('<Command-x>', delete_file)
else:
    root.bind('<Control-s>', save_text)
    root.bind('<Control-x>', delete_file)  

root.mainloop()
