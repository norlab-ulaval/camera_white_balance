import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import sys

def target_white_to_black():
    number_cols = 15
    cmap = plt.get_cmap("Greys")(np.linspace(0,1,number_cols))

    fig = plt.figure(figsize=(20,15), dpi=500)
    ax = fig.add_subplot()
    for i in range(0, number_cols):
        rect = patches.Rectangle((0 + (i*10),0), 10 + (i*10), 100, facecolor=cmap[i])
        ax.add_patch(rect)

    ax.set_xlim([0,(10*number_cols)])
    ax.set_ylim([0,100])
    ax.set_axis_off()
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
    plt.savefig("white_balance_target_white_to_black.pdf")
    plt.show()

def target_gray():
    fig = plt.figure(figsize=(20,15), dpi=500)
    ax = fig.add_subplot()
    rect = patches.Rectangle((0,0), 100, 100, facecolor="gray")
    ax.add_patch(rect)
    ax.set_xlim([0,100])
    ax.set_ylim([0,100])
    ax.set_axis_off()
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
    plt.savefig("white_balance_gray.pdf")
    plt.show()

def main():
    if sys.argv[1] == "white_to_black":
        target_white_to_black()
    elif sys.argv[1] == "gray":
        target_gray()

if __name__ == "__main__":
    main()

