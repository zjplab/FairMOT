import numpy as np 

def tlbr_occlution(tlbr1, tlbr2):
    """(min x, min y, max x, max y)`, i.e.,
    `(top left, bottom right)`.

    -> calculate their overlap
    """
    in_w=max(.0, min(tlbr2[2], tlbr1[2]) - max(tlbr1[0], tlbr2[0]))
    in_h=max(.0, min(tlbr2[3],tlbr2[3]) - max(tlbr1[1], tlbr2[1]))
    inter= in_w * in_h
    S_1= (tlbr1[3]-tlbr1[1])*(tlbr1[2]-tlbr1[0])
    S_2=(tlbr2[3]- tlbr2[1])*(tlbr2[2]-tlbr2[0])
    return (inter/S_1, inter/S_2)


if __name__=='__main__':
    tlbr1=[0, 0, 7, 5]
    tlbr2=[3, 3, 9, 7]
    print(tlbr_occlution(tlbr1, tlbr2))
    #(0.45714285714285713, 0.6666666666666666)