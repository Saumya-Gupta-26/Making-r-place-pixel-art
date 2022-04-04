from PIL import Image
import numpy as np

black = [0,0,0]
orange = [255,214,53] #   FFD635

def set_black(npimg, x, y):
    npimg[x,y,0] = black[0]
    npimg[x,y,1] = black[1]
    npimg[x,y,2] = black[2]

def set_orange(npimg, x, y):
    npimg[x,y,0] = orange[0]
    npimg[x,y,1] = orange[1]
    npimg[x,y,2] = orange[2]


def main():
    myimg = np.asarray(Image.new(mode="RGB", size=(17,15), color=(255,255,255)))

    for ind in range(17):
        set_black(myimg, 0, ind)
        set_black(myimg, 14, ind)

    for ind in range(15):
        set_black(myimg, ind, 0)
        set_black(myimg, ind, 16)

    for ind in range(5):
        set_orange(myimg, 9, ind+6)
        set_orange(myimg, 11, ind+6)
        set_black(myimg, 8, ind+6)
        set_black(myimg, 10, ind+6)
        set_black(myimg, 12, ind+6)

    for ind in range(3):
        set_black(myimg, 3, ind+3)
        set_black(myimg, 3, ind+11)
        set_black(myimg, 7, ind+3)
        set_black(myimg, 7, ind+11)
        set_black(myimg, ind+4, 2)
        set_black(myimg, ind+4, 6)
        set_black(myimg, ind+4, 10)
        set_black(myimg, ind+4, 14)
        set_black(myimg, ind+9, 5)
        set_black(myimg, ind+9, 11)

    set_black(myimg, 2,2)
    set_black(myimg, 2,6)
    set_black(myimg, 2,10)
    set_black(myimg, 2,14)
    set_black(myimg, 5,4)
    set_black(myimg, 5,12)
    set_black(myimg, 2,4)
    set_black(myimg, 2,12)

    data = Image.fromarray(myimg)
    data.save("image-tiny.png")



if __name__ == "__main__":
    main()
