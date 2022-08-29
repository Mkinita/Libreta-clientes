from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Hola mundo: treeview')
 
tree= ttk.Treeview(root)
tree['columns'] = ('Nombre','Telefono','Empresa')

tree.column('#0',width=0, stretch=NO)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

tree.heading ('#0', text='id')
tree.heading ('Nombre', text='Nombre')
tree.heading ('Telefono', text='Telefono')
tree.heading ('Empresa', text='Empresa')

tree.grid(column=0,row=0)

tree.insert('',END,'lala',values=('uno','dos','tres'),text='carlos jerez')
tree.insert('',END,'lele',values=('cuatr','cinco','seis'),text='rodrigo jerez')
tree.insert('lele',END,'lili',values=('4','5','4'),text='hijo jerez')

root.mainloop()