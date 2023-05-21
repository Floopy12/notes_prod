import tkinter as tk
from tkinter import *
from tkinter import ttk
from oop import Save, Delete
from base import cur, con



win = tk.Tk()

win.title('Note')
win.geometry('700x500+370+100')

photo = tk.PhotoImage(file = 'notepaper.png')
win.iconphoto(False , photo)
win.resizable(False, False)
win.config()




frame_aside = tk.Frame(win, width = 300, height = 500, bg = '#c9efb7')
frame_aside.grid(row = 0, column = 0, sticky = 'nsew')

frame_fields = tk.Frame(win, width = 300, height = 500, bg = '#c9efb7')
frame_fields.grid(row = 0, column = 1, sticky = 'nswe')

frame_footer = tk.Frame(win, width = 700, height = 100, bg = '#c9efb7')
frame_footer.grid(row = 1, column = 0, columnspan = 2,sticky='nswe')


label_allnotes = tk.Label(frame_aside, text = 'Ваши заметки', font = 'Helvetica 10 bold', bg = '#c9efb7')
label_allnotes.pack(pady = 12)


def delete_note():
    select = list_note.curselection()  #индекс выбраного элемента
    name_note = list_note.get(select)   #имя заметки по индексу
    cur.execute(f'DELETE FROM note WHERE name = "{name_note}"')
    con.commit()
    list_note.delete(select)


def show_note():
    select = list_note.curselection()
    name_note = list_note.get(select)
    text_note = cur.execute(f'SELECT content FROM note WHERE name = "{name_note}"').fetchone()
    field_content.delete('1.0', END)
    field_name.insert(1.0, name_note)
    field_content.insert(1.0, text_note)
   

but_delete = tk.Button(frame_aside, text = 'Удалить заметку', command = delete_note)
but_delete.pack(fill = X, side = BOTTOM )

but_show = tk.Button(frame_aside, text = 'Открыть заметку', command = show_note)
but_show.pack(fill = X)



    
all = cur.execute('SELECT name FROM note WHERE rowid > 0').fetchall()
all_var = Variable(value=all)

    
list_note = tk.Listbox(frame_aside, listvariable = all_var ,
                        bg = '#a0dff0',
                        relief = 'raised', 
                        font = 'Helvetica 12 normal',
                        )

list_note.pack(side=RIGHT, fill=BOTH, expand=1)


scroll = ttk.Scrollbar(frame_aside, orient = 'vertical', command = list_note.yview)
scroll.pack(side = tk.LEFT, fill = tk.Y)

list_note["yscrollcommand"] = scroll.set



label_name = tk.Label(frame_fields, text = 'Имя заметки', font = 'Helvetica 10 bold', bg = '#c9efb7')
label_name.grid(row = 0, column = 0, pady = 12, columnspan = 2, sticky = 'w', padx = 30)

field_name = tk.Text(frame_fields,
                     width = 20,
                     height = 1,
                     bg = '#d6f8f7',
                     font = 8)
field_name.grid(row = 0, column = 0, pady = 8, sticky = 'ns')


field_content = tk.Text(frame_fields,
                        width = 60,
                        height = 23, 
                        bg = '#d6f8f7',
                        font = 'Helvetica 11')
field_content.grid(row = 3, column = 0, padx = 5)


save_content = Save(field_name, field_content)   # Сохраняем заметку в бд

but_save = tk.Button(frame_fields, text = 'Сохранить', command = save_content.save_text, width = 20)
but_save.grid(row = 4, column = 0, sticky='e', pady = 8)




delete_content = Delete(field_name, field_content)  # Удаляем заметку из бд

but_clear = tk.Button(frame_fields, text = 'Очистить', command = delete_content.delete_text, width = 20)
but_clear.grid(row = 4, column = 0, sticky='w', columnspan = 2, padx = 5)






win.mainloop()