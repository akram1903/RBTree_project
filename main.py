import random
import time
import sys
from red_black_tree import RBTree
from red_black_node import *
from tkinter import *
# https://github.com/akram1903/RBTree_project.git


def load():
    print('loading')
    if tree1.root is not None:
        print('\n\nThe file has been loaded before')
        return None
    i = 0
    with open("EN-US-Dictionary.txt") as file:
        for item in file:
            i += 1
            # print(i)
            value = item.strip().lower()
            tree1.insert_RB_way(value)
    print('load done')
    label_size = Label(window, text='size is ' + str(tree1.size), bg='#687a7d')
    label_size.place(x=10, y=250)

    label_height = Label(window, text='depth is ' + str(tree1.get_depth_naiveBST()), bg='#687a7d')
    label_height.place(x=170, y=250)
    window.update_idletasks()
    # arr = random.sample(range(1, 100), 15)
    # arr = [29, 64, 93, 15, 73, 27, 22, 11, 84, 4, 94, 89, 52, 30, 39]
    # print(arr)
    # for i in range(15):
    #     tree1.insert_RB_way(arr[i])
    #     tree1.print2D(tree1.root)
    #     print(i, '=============================================================')

    # tree1.print_inorder()


def insert():
    if entry.get() == '':
        s = " you haven't fill the text field        \n"
        print(s)
        label_search = Label(window, text=s, bg='#687a7d', fg='red')
        label_search.place(x=250, y=100)
        return None
    ip = entry.get().strip()

    if tree1.root is not None:
        result = tree1.search(ip)
    if tree1.root is not None and result[1] == 1:
        s = str(entry.get()) + ' is already inserted                    '
        print(s)
        label_search = Label(window, text=s, bg='#687a7d', fg='red')
        label_search.place(x=250, y=100)
        return 0
    else:
        print('inserting ', entry.get())
        print(tree1.size)
        if ip.isalpha():
            ip = ip.lower().strip()
        else:
            ip = float(ip)
        tree1.insert_RB_way(ip)
        s = str(ip)+" inserted successfully"
        print(s)
        label_search = Label(window, text=s, bg='#687a7d')
        label_search.place(x=250, y=100)
        print(tree1.size)
    label_size = Label(window, text='size is ' + str(tree1.size), bg='#687a7d')
    label_size.place(x=10, y=250)

    label_height = Label(window, text='depth is ' + str(tree1.get_depth_naiveBST()), bg='#687a7d')
    label_height.place(x=170, y=250)
    window.update_idletasks()


def search():
    if tree1.root is None:
        s = "the file haven't been loaded yet"
        print(s)
        label_search = Label(window, text=s, bg='#687a7d', fg='red')
        label_search.place(x=250, y=100)
        return None
    elif entry.get() == '':
        s = " you haven't fill the search field\n"
        print(s)
        label_search = Label(window, text=s, bg='#687a7d', fg='red')
        label_search.place(x=250, y=100)
        return None
    ip = entry.get()
    if ip.isnumeric():
        ip = float(ip)
    else:
        ip = ip.lower().strip()
    result = tree1.search(ip)

    if result[1] == 1:
        node = result[0]
        s = "found "+str(node)+'                             \n\n'
        print("\nfound ", node, sep='\n', end='\n\n')
    else:
        s = "not found\n maybe you mean " + str(result[0]) + '??'
        print(ip, "not found, maybe you mean ", result[0], ' ??', end='\n\n')
    label_search = Label(window, text=s, bg='#687a7d')
    label_search.place(x=250, y=100)

    window.update_idletasks()


# sys.setrecursionlimit(20000)
tree1 = RBTree(None)
loaded = False
window = Tk()
window.geometry("420x320")
window.title("red black tree dictionary")
window.config(background="#687a7d")

load_button = Button(window,
                     text="load",
                     command=load,
                     fg="black",
                     bg="#0b5557",
                     width=10)

load_button.place(x=170,
                  y=50)
search_button = Button(window,
                       text="search",
                       command=search,
                       fg="black",
                       bg="#0b5557",
                       width=10)
search_button.place(x=170,
                    y=100)

insert_button = Button(window,
                       text="insert",
                       command=insert,
                       fg="black",
                       bg="#0b5557",
                       width=10)
insert_button.place(x=170,
                    y=150)

entry = Entry(window)
entry.place(x=10,
            y=100)

# label_size = Label(window, text='size is '+str(tree1.size), bg='#687a7d')
# label_size.place(x=10, y=250)
window.mainloop()


print("\n\nTree depth is  "+str(tree1.get_depth_naiveBST()))
print("Tree size is "+str(tree1.size))
# tree1.print_inorder()
# tree1.print2D(tree1.root)
# tree1.check_red_black_tree()
