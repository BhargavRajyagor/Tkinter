import tkinter as tk

root = tk.Tk()
box = tk.Listbox(root)
box.insert(tk.END, 'First')
box.insert(tk.END, 'Second')
box.insert(tk.END, 'Third')
box.pack()

box2 = tk.Listbox(root)
box2.insert(tk.END, 'First')
box2.insert(tk.END, 'Second')
box2.insert(tk.END, 'Third')
box2.pack()


def on_first_box(idx, val):
    print('First box idx: %s, value: %s' % (idx, val))


def on_second_box(idx, val):
    print('Second box idx: %s, value: %s' % (idx, val))


def onselect(event, listbox):
    w = event.widget
    try:
        idx = int(w.curselection()[0])
    except IndexError:
        return
    if listbox is box:
        return on_first_box(idx, w.get(idx))
    if listbox is box2:
        return on_second_box(idx, w.get(idx))


box.bind('<<ListboxSelect>>', lambda e: onselect(e, box))
box2.bind('<<ListboxSelect>>', lambda e: onselect(e, box2))

root.mainloop()