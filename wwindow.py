import tkinter as tk
from oop import Save, Delete
from base import cur, con



win = tk.Tk()

win.title('Note')
win.geometry('800x700')

photo = tk.PhotoImage(file = 'notepaper.png')
win.iconphoto(False , photo)
win.config(bg = '#c9efb7')

field_name = tk.Text(win, 
                     width = 15,
                     height = 1)
field_name.pack()

field_content = tk.Text(win,
                 width = 50,
                 height = 10
                 )

field_content.pack()

save_content = Save(field_name, field_content)


but_save = tk.Button(win, text = 'Save text', command = save_content.save_text)
but_save.pack()

delete_content = Delete(field_name, field_content)

but_delete = tk.Button(win, text = 'Delete text', command = delete_content.delete_text)
but_delete.pack()




win.mainloop()