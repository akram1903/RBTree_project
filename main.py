import time
import sys
from red_black_tree import RBTree
from red_black_node import *
from tkinter import *
# https://github.com/akram1903/RBTree_project.git


def load():
    i = 0
    # with open("EN-US-Dictionary.txt") as file:
    #     for item in file:
    #         value = item.strip()
    #         tree1.insert_RB_way(value.lower())
            # if i == 5:
            #     break
            # i += 1
            # tree1.print_inorder()
            # print(i,
            #       '__________________________________________________________________________________________________')
            # i += 1
            # tree1.print2D(tree1.root)

    for i in range(100000, 0, -1):
        tree1.insert_RB_way(i)
        print(i)
    tree1.print_inorder()


def insert():
    pass


def search():
    ip = entry.get()
    if ip.isalpha():
        ip = ip.lower().strip()
    else:
        ip = float(ip)
    result = tree1.search(ip)

    if result[1] == 1:
        if result[0].value > ip:
            node = result[0].left
        else:
            node = result[0].right

        print("\nfound ", node, sep='\n', end='\n\n')
    else:
        print("not found, maybe you mean ", result[0], ' ??', end='\n\n')


# sys.setrecursionlimit(98000)
tree1 = RBTree(None)

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

print("Tree depth is  "+str(tree1.get_depth_naiveBST()))

# tree1.print_inorder()
tree1.print2D(tree1.root)
# tree1.check_red_black_tree()
