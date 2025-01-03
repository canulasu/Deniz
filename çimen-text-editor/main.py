import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import platform
import os

# define key variables

mode = 'light'

# define functions

class menu_functions():

    def about_text():
        messagebox.showinfo('About', 'Deniz Çimen Text Editor V.0.0.2')

def delete_file(event=None): 
    filename = save_query_box.get('1.0', tk.END).strip()
    try:
        os.remove(filename)
        load_text_to_entry()

    except FileNotFoundError:
        messagebox.showinfo('Error', 'File not found!')

def syantax_on(event=None):

    main_text_box.tag_remove('highlight_print', '1.0', tk.END)
    main_text_box.tag_remove('highlight_true', '1.0', tk.END)
    main_text_box.tag_remove('highlight_false', '1.0', tk.END)

    start = '1.0'

    while True:
        pos = main_text_box.search('print', start, stopindex=tk.END, nocase=True)

        if not pos:
            break

        end = f"{pos}+{len('print')}c"

        main_text_box.tag_add('highlight_print', pos, end)
        start = end


        pos = main_text_box.search('True', start, stopindex=tk.END, nocase=True)

        if not pos:
            break

        end = f"{pos}+{len('True')}c"

        main_text_box.tag_add('highlight_true', pos, end)
        start = end

        pos = main_text_box.search('False', start, stopindex=tk.END, nocase=True)

        if not pos:
            break

        end = f"{pos}+{len('False')}c"

        main_text_box.tag_add('highlight_false', pos, end)
        start = end
        
    main_text_box.tag_config('highlight_true', foreground='blue')
    main_text_box.tag_config('highlight_false', foreground='blue')
    main_text_box.tag_config('highlight_print', foreground='yellow')

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

def choose_file():
    file_path = filedialog.askopenfilename(title='Choose a file', filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

    if file_path:
        save_query_box.delete('1.0', tk.END)
        save_query_box.insert('1.0', file_path)
    else:
        pass

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
    menu.geometry('200x400')

    about_button = tk.Button(menu, text='About', command=menu_functions.about_text)
    about_button.pack(pady=10, padx=10)

    color_button = tk.Button(menu, text='Change Color', command=change_color_profile)
    color_button.pack(pady=10, padx=10)

    color_button = tk.Button(menu, text='Update Syntax', command=syantax_on)
    color_button.pack(pady=10, padx=10)

    color_button = tk.Button(menu, text='Run Code', command=execute_code)
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
        root.configure(bg='black')
        top_frame.configure(bg='black')
        mode = 'dark'

    elif mode == 'dark':
        main_text_box.configure(bg='white')
        main_text_box.configure(fg='black')
        save_query_box.configure(bg='white')
        save_query_box.configure(fg='black')
        root.configure(bg='white')
        top_frame.configure(bg='white')
        mode = 'light'

def execute_code():

    if save_query_box.get('1.0', tk.END).strip() == '':
        messagebox.showinfo('Error', 'File Does Not Exist')

    elif '.py' in save_query_box.get('1.0', tk.END).strip():
        if platform.system() == 'Darwin':
            os.system(f'python3 {save_query_box.get("1.0", tk.END).strip()}')
        elif platform.system() == 'Linux':
            os.system(f'python3 {save_query_box.get("1.0", tk.END).strip()}')
        elif platform.system() == 'Windows':
            os.system(f'python {save_query_box.get("1.0", tk.END).strip()}')

    elif '.rb' in save_query_box.get('1.0', tk.END).strip():
        os.system(f'ruby {save_query_box.get("1.0", tk.END).strip()}')

    elif '.js' in save_query_box.get('1.0', tk.END).strip():
        os.system(f'node {save_query_box.get("1.0", tk.END).strip()}')

    elif '.lua' in save_query_box.get('1.0', tk.END).strip():
        os.system(f'lua {save_query_box.get("1.0", tk.END).strip()}')

    elif '.pl' in save_query_box.get('1.0', tk.END).strip():
        os.system(f'perl {save_query_box.get("1.0", tk.END).strip()}')
    
    else:
        messagebox.showinfo('Error', 'Language Not Yet Supported')

root = tk.Tk()

root.title('Çimen Text Editor')
root.geometry('1024x768')

top_frame = tk.Frame(root)
top_frame.pack(side='top', anchor='nw', pady=10, padx=10, fill='x')

save_button = tk.Button(top_frame, text='Save', command=save_text)
save_button.pack(side='left', padx=10)

refresh_button = tk.Button(top_frame, text='Refresh', command=load_text_to_entry)
refresh_button.pack(side='left', padx=10)

menu_button = tk.Button(top_frame, text='Menu', command=load_menu)
menu_button.pack(side='left', padx=10)

menu_button = tk.Button(top_frame, text='Choose File', command=choose_file)
menu_button.pack(side='left', padx=10)

save_query_box = tk.Text(top_frame, width=40, height=1)
save_query_box.pack(side='right', padx=10)

main_text_box = tk.Text(root, width=40, height=20)
main_text_box.pack(pady=10, padx=10, expand=True, fill='both')

if platform.system() == 'Darwin':
    root.bind('<Command-s>', save_text)
    root.bind('<Command-d>', delete_file)
else:
    root.bind('<Control-s>', save_text)
    root.bind('<Control-d>', delete_file)  

root.mainloop()
