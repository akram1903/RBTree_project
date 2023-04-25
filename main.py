import random
import time
import sys
from red_black_tree import RBTree
from red_black_node import *
from tkinter import *
# https://github.com/akram1903/RBTree_project.git


def load():
    if tree1.root is not None:
        print('\n\nThe file has been loaded before')
        return None
    i = 0
    with open("EN-US-Dictionary.txt") as file:
        for item in file:
            i += 1
            print(i,
                  '__________________________________________________________________________________________________')
            value = item.strip().lower()
            tree1.insert_RB_way(value)
            # if i == 100:
            #     break
            # tree1.print2D(tree1.root)

    # arr = random.sample(range(1, 100), 15)
    # arr = [29, 64, 93, 15, 73, 27, 22, 11, 84, 4, 94, 89, 52, 30, 39]
    # print(arr)
    # for i in range(15):
    #     tree1.insert_RB_way(arr[i])
    #     tree1.print2D(tree1.root)
    #     print(i, '=============================================================')

    # tree1.print_inorder()

    # for i in range(1, 100):
    #     tree1.insert_RB_way(i)
    #     print(i)
    #     tree1.print2D(tree1.root)
    #     print(i, '----------------------------')
    # tree1.print_inorder()

    # tree1.insert_RB_way(3)
    # tree1.insert_RB_way(4)
    # tree1.print2D(tree1.root)
    # tree1.insert_RB_way(1)
    # tree1.insert_RB_way(2)
    # tree1.print2D(tree1.root)
    # tree1.insert_RB_way('younis')
    # tree1.print2D(tree1.root)
    # print('----------------------------------------------')
    # tree1.insert_RB_way('yehia')
    # tree1.print2D(tree1.root)
    # print('----------------------------------------------')
    # tree1.insert_RB_way('akram')
    # tree1.print2D(tree1.root)
    # print('----------------------------------------------')
    # tree1.insert_RB_way('arkhmedes')
    # tree1.print2D(tree1.root)
    # print('----------------------------------------------')
    # tree1.insert_RB_way(74)
    # tree1.print2D(tree1.root)


def insert():

    ip = entry.get().strip()
    result = tree1.search(ip)
    if result[1] == 1:
        print(entry.get(), ' is already inserted')
        return 0
    else:
        print('inserting ', entry.get())
        print(tree1.size)
        if ip.isalpha():
            ip = ip.lower().strip()
        else:
            ip = float(ip)
        tree1.insert_RB_way(ip)
        print(ip, 'inserted successfully')
        print(tree1.size)


def search():
    ip = entry.get()
    if ip.isnumeric():
        ip = float(ip)
    else:
        ip = ip.lower().strip()
    result = tree1.search(ip)

    if result[1] == 1:
        node = result[0]

        print("\nfound ", node, sep='\n', end='\n\n')
    else:
        print(ip, "not found, maybe you mean ", result[0], ' ??', end='\n\n')


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

window.mainloop()

# tree1.insert_RB_way('Rockne'.lower())
# tree1.insert_RB_way('wimpiest')
# tree1.insert_RB_way('loop')
# tree1.insert_RB_way('Fargo')
# tree1.insert_RB_way('so5n')
# tree1.insert_RB_way('sban')

# Rockne's
# wimpiest
# loop's
# Fargo

# for i in range(1, 10):
#     print(i)
#     tree1.insert_RB_way(i)

print("\n\nTree depth is  "+str(tree1.get_depth_naiveBST()))
print("Tree size is "+str(tree1.size))
# tree1.print_inorder()
# tree1.print2D(tree1.root)
# tree1.check_red_black_tree()
