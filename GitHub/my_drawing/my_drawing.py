"""
File: my_drawing.py
Name: Luna
----------------------
TODO: This program draws my favorite character in BT21!
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: CHIMMY

    七米是我BT21最愛的角色
    一隻穿著黃色Hoodie的白色的狗
    吐舌頭是他的靈魂也是最有魅力的地方！
    """
    window = GWindow(width=960, height=1355)
    # background
    bg = GRect(960, 1355)
    bg.filled = True
    bg.color = 'lemonchiffon'
    bg.fill_color = 'lemonchiffon'
    window.add(bg)
    # name
    name_bg = GRect(409, 111)
    name_bg.filled = True
    name_bg.color = 'lightseagreen'
    name_bg.fill_color = 'lightseagreen'
    window.add(name_bg, x=269, y=18)
    name = GLabel('CHIMMY')
    name.font = 'Courier-100-bold-italic'
    window.add(name, x=290, y=126)
    deco_l = GRect(181, 10)
    deco_l.filled = True
    window.add(deco_l, x=41, y=74)
    deco_r = GRect(181, 10)
    deco_r.filled = True
    window.add(deco_r, x=723, y=74)
    # left ear
    ear_l_upper = GPolygon()
    ear_l_upper.add_vertex((380, 555))
    ear_l_upper.add_vertex((312, 636))
    ear_l_upper.add_vertex((369, 671))
    window.add(ear_l_upper)
    ear_l_upper.filled = True
    ear_l_lower = GOval(85, 155)
    ear_l_lower.filled = True
    window.add(ear_l_lower, x=297, y=618)
    # head
    head = GOval(300, 244)
    head.filled = True
    head.color = 'gold'
    head.fill_color = 'gold'
    window.add(head, x=336, y=519)
    cheek = GOval(302, 158)
    cheek.filled = True
    cheek.color = 'gold'
    cheek.fill_color = 'gold'
    window.add(cheek, x=325, y=652)
    # face
    face = GOval(222, 180)
    face.filled = True
    face.color = 'white'
    face.fill_color = 'white'
    window.add(face, x=376, y=602)
    eye_l = GOval(17, 19)
    eye_l.filled = True
    window.add(eye_l, x=453, y=675)
    eye_r = GOval(19, 19)
    eye_r.filled = True
    window.add(eye_r, x=504, y=670)
    nose = GOval(24, 13)
    nose.filled = True
    window.add(nose, x=476, y=694)
    mouth = GLine(x0=455, y0=728, x1=530, y1=715)
    window.add(mouth)
    tongue = GArc(26, 52, 187, 184)
    tongue.filled = True
    tongue.fill_color = 'salmon'
    window.add(tongue, x=503, y=703)
    tongue_mid = GLine(x0=514, y0=718, x1=516, y1=729)
    window.add(tongue_mid)
    # right ear
    ear_r_upper = GPolygon()
    ear_r_upper.add_vertex((597, 559))
    ear_r_upper.add_vertex((582, 668))
    ear_r_upper.add_vertex((656, 626))
    window.add(ear_r_upper)
    ear_r_upper.filled = True
    ear_r_lower = GOval(90, 160)
    ear_r_lower.filled = True
    window.add(ear_r_lower, x=581, y=606)
    # brand
    brand_bg = GRect(186, 86)
    brand_bg.filled = True
    window.add(brand_bg, x=718, y=1246)
    brand = GLabel('BT21')
    brand.font = 'Verdana-60-bold'
    brand.color = 'white'
    window.add(brand, x=727, y=1324)
    # heart1
    heart1_l = GOval(65, 35)
    heart1_l.filled = True
    heart1_l.color = 'lightcoral'
    heart1_l.fill_color = 'lightcoral'
    window.add(heart1_l, x=131, y=488)
    heart1_r = GOval(34, 62)
    heart1_r.filled = True
    heart1_r.color = 'lightcoral'
    heart1_r.fill_color = 'lightcoral'
    window.add(heart1_r, x=166, y=457)
    # heart2
    heart2_l = GOval(35, 18)
    heart2_l.filled = True
    heart2_l.color = 'tomato'
    heart2_l.fill_color = 'tomato'
    window.add(heart2_l, x=225, y=516)
    heart2_r = GOval(18, 35)
    heart2_r.filled = True
    heart2_r.color = 'tomato'
    heart2_r.fill_color = 'tomato'
    window.add(heart2_r, x=245, y=496)
    # heart3
    heart3_l = GOval(33, 72)
    heart3_l.filled = True
    heart3_l.color = 'indianred'
    heart3_l.fill_color = 'indianred'
    window.add(heart3_l, x=602, y=396)
    heart3_r = GOval(70, 38)
    heart3_r.filled = True
    heart3_r.color = 'indianred'
    heart3_r.fill_color = 'indianred'
    window.add(heart3_r, x=606, y=435)
    # deco
    line1 = GLine(x0=56, y0=724, x1=255, y1=739)
    window.add(line1)
    line2 = GLine(x0=60, y0=514, x1=306, y1=625)
    window.add(line2)
    line3 = GLine(x0=125, y0=358, x1=347, y1=553)
    window.add(line3)
    line4 = GLine(x0=410, y0=353, x1=435, y1=472)
    window.add(line4)
    line5 = GLine(x0=535, y0=482, x1=565, y1=368)
    window.add(line5)
    line6 = GLine(x0=635, y0=518, x1=824, y1=386)
    window.add(line6)
    line7 = GLine(x0=722, y0=584, x1=904, y1=535)
    window.add(line7)
    line8 = GLine(x0=733, y0=690, x1=922, y1=700)
    window.add(line8)
    line9 = GLine(x0=733, y0=802, x1=851, y1=826)
    window.add(line9)
    line10 = GLine(x0=610, y0=871, x1=716, y1=1020)
    window.add(line10)
    line11 = GLine(x0=268, y0=926, x1=156, y1=1032)
    window.add(line11)
    line12 = GLine(x0=257, y0=833, x1=39, y1=924)
    window.add(line12)
    line13 = GLine(x0=433, y0=845, x1=396, y1=1083)
    window.add(line13)
    line14 = GLine(x0=545, y0=888, x1=561, y1=1034)
    window.add(line14)
    # star1
    star1_1 = GLine(x0=276, y0=849, x1=282, y1=973)
    star1_1.color = 'darkturquoise'
    window.add(star1_1)
    star1_2 = GLine(x0=227, y0=896, x1=323, y1=898)
    star1_2.color = 'darkturquoise'
    window.add(star1_2)
    star1_3 = GLine(x0=251, y0=877, x1=313, y1=928)
    star1_3.color = 'darkturquoise'
    window.add(star1_3)
    star1_4 = GLine(x0=320, y0=848, x1=232, y1=951)
    star1_4.color = 'darkturquoise'
    window.add(star1_4)
    # star2
    star2_1 = GLine(x0=33, y0=806, x1=135, y1=792)
    star2_1.color = 'teal'
    window.add(star2_1)
    star2_2 = GLine(x0=80, y0=755, x1=80, y1=853)
    star2_2.color = 'teal'
    window.add(star2_2)
    star2_3 = GLine(x0=53, y0=777, x1=113, y1=822)
    star2_3.color = 'teal'
    window.add(star2_3)
    star2_4 = GLine(x0=119, y0=747, x1=43, y1=847)
    star2_4.color = 'teal'
    window.add(star2_4)
    # diamond
    arc1 = GArc(98, 112, 270, 90)
    arc1.color = 'darkcyan'
    window.add(arc1, x=743, y=828)
    arc2 = GArc(90, 132, 180, 90)
    arc2.color = 'darkcyan'
    window.add(arc2, x=792, y=826)
    arc3 = GArc(98, 116, 0, 90)
    arc3.color = 'darkcyan'
    window.add(arc3, x=741, y=884)
    arc4 = GArc(102, 102, 90, 90)
    arc4.color = 'darkcyan'
    window.add(arc4, x=789, y=892)


if __name__ == '__main__':
    main()
