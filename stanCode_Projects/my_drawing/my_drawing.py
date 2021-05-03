"""
File: Dear Basketball
Name: Danny
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    In memory of KOBE BRYANT, one of the best sports player of all time.
    """
    window = GWindow(width=800, height=400, title='Dear Basketball')
    black = GRect(800, 360)
    black.filled = True
    black.fill_color = 'black'
    window.add(black, 0, 20)
    purple_1 = GRect(400, 20)
    purple_1.filled = True
    purple_1.fill_color = 'purple'
    purple_1.color = 'purple'
    window.add(purple_1, 400, 0)
    purple_2 = GRect(400, 20)
    purple_2.filled = True
    purple_2.fill_color = 'purple'
    purple_2.color = 'purple'
    window.add(purple_2, 0, 380)
    gold_1 = GRect(400, 20)
    gold_1.filled = True
    gold_1.fill_color = 'gold'
    gold_1.color = 'gold'
    window.add(gold_1, 0, 0)
    gold_2 = GRect(400, 20)
    gold_2.filled = True
    gold_2.fill_color = 'gold'
    gold_2.color = 'gold'
    window.add(gold_2, 400, 380)

    mamba_left_upper = GPolygon()
    mamba_left_upper.add_vertex((60, 145))
    mamba_left_upper.add_vertex((70, 140))
    mamba_left_upper.add_vertex((130, 170))
    mamba_left_upper.add_vertex((130, 190))
    mamba_left_upper.filled = True
    mamba_left_upper.fill_color = 'white'
    window.add(mamba_left_upper)
    # x = 133 (mid)
    mamba_right_upper = GPolygon()
    mamba_right_upper.add_vertex((206, 145))
    mamba_right_upper.add_vertex((196, 140))
    mamba_right_upper.add_vertex((136, 170))
    mamba_right_upper.add_vertex((136, 190))
    mamba_right_upper.filled = True
    mamba_right_upper.fill_color = 'white'
    window.add(mamba_right_upper)

    mamba_left_lower = GPolygon()
    mamba_left_lower.add_vertex((130, 200))
    mamba_left_lower.add_vertex((105, 218))
    mamba_left_lower.add_vertex((65, 175))
    mamba_left_lower.add_vertex((60, 155))
    mamba_left_lower.filled = True
    mamba_left_lower.fill_color = 'white'
    window.add(mamba_left_lower)

    mamba_right_lower = GPolygon()
    mamba_right_lower.add_vertex((136, 200))
    mamba_right_lower.add_vertex((161, 218))
    mamba_right_lower.add_vertex((201, 175))
    mamba_right_lower.add_vertex((206, 155))
    mamba_right_lower.filled = True
    mamba_right_lower.fill_color = 'white'
    window.add(mamba_right_lower)

    mamba_left_down = GPolygon()
    mamba_left_down.add_vertex((130, 210))
    mamba_left_down.add_vertex((130, 330))
    mamba_left_down.add_vertex((118, 322))
    mamba_left_down.add_vertex((108, 227))
    mamba_left_down.filled = True
    mamba_left_down.fill_color = 'white'
    window.add(mamba_left_down)

    mamba_right_down = GPolygon()
    mamba_right_down.add_vertex((136, 210))
    mamba_right_down.add_vertex((136, 330))
    mamba_right_down.add_vertex((148, 322))
    mamba_right_down.add_vertex((158, 227))
    mamba_right_down.filled = True
    mamba_right_down.fill_color = 'white'
    window.add(mamba_right_down)

    number_24 = GLabel('8')
    number_24.color = 'purple'
    number_24.font = 'Baskerville-80-bold'
    window.add(number_24, 70, 150)

    number_24 = GLabel('24')
    number_24.color = 'gold'
    number_24.font = 'Baskerville-80-bold'
    window.add(number_24, 120, 150)

    head = GOval(22, 22)
    head.filled = True
    head.fill_color = 'white'
    head.color = 'white'
    window.add(head, 355, 105)

    ball = GOval(24, 24)
    ball.filled = True
    ball.fill_color = 'white'
    ball.color = 'white'
    window.add(ball, 380, 75)

    body = GPolygon()
    body.add_vertex((350, 125))
    body.add_vertex((365, 165))
    body.add_vertex((395, 163))
    body.add_vertex((380, 123))
    body.filled = True
    body.fill_color = 'white'
    body.color = 'white'
    window.add(body)

    arc_1 = GArc(15, 15, 220, 135)
    arc_1.color = 'black'
    window.add(arc_1, 360, 120)
    arc_1_1 = GArc(15, 15, 220, 135)
    arc_1_1.color = 'black'
    window.add(arc_1_1, 360, 121)

    right_arm = GPolygon()
    right_arm.add_vertex((380, 123))
    right_arm.add_vertex((403, 115))
    right_arm.add_vertex((393, 95))
    right_arm.add_vertex((400, 95))
    right_arm.add_vertex((415, 120))
    right_arm.add_vertex((380, 133))
    right_arm.filled = True
    right_arm.fill_color = 'white'
    right_arm.color = 'white'
    window.add(right_arm)

    left_arm = GPolygon()
    left_arm.add_vertex((375, 123))
    left_arm.add_vertex((390, 95))
    left_arm.add_vertex((395, 95))
    left_arm.add_vertex((385, 125))
    left_arm.filled = True
    left_arm.fill_color = 'white'
    left_arm.color = 'white'
    window.add(left_arm)

    arc_2 = GArc(100, 100, 260, 80)
    arc_2.color = 'white'
    window.add(arc_2, 360, 95)

    arc_3 = GArc(100, 100, 260, 80)
    arc_3.color = 'white'
    window.add(arc_3, 358, 92)

    arc_4 = GArc(200, 200, 345, 60)
    arc_4.filled = True
    arc_4.fill_color = 'white'
    arc_4.color = 'white'
    window.add(arc_4, 295, 105)

    black_fix1 = GArc(200, 200, 353, 45)
    black_fix1.filled = True
    black_fix1.fill_color = 'black'
    black_fix1.color = 'black'
    window.add(black_fix1, 262, 124)

    left_shoulder_black1 = GOval(10, 10)
    left_shoulder_black1.filled = True
    left_shoulder_black1.fill_color = 'black'
    left_shoulder_black1.color = 'black'
    window.add(left_shoulder_black1, 346, 122)
    left_shoulder_black2 = GOval(30, 30)
    left_shoulder_black2.filled = True
    left_shoulder_black2.fill_color = 'black'
    left_shoulder_black2.color = 'black'
    window.add(left_shoulder_black2, 330, 126)
    left_shoulder_white1 = GArc(60, 60, 150, 70)
    left_shoulder_white1.filled = True
    left_shoulder_white1.fill_color = 'white'
    left_shoulder_white1.color = 'white'
    window.add(left_shoulder_white1, 357, 118)

    leg_1 = GArc(200, 200, 170, 45)
    leg_1.filled = True
    leg_1.fill_color = 'white'
    leg_1.color = 'white'
    window.add(leg_1, 364, 133)

    leg_2_black = GRect(20, 30)
    leg_2_black.filled = True
    leg_2_black.fill_color = 'black'
    leg_2_black.color = 'black'
    window.add(leg_2_black, 396, 165)

    leg_central = GPolygon()
    leg_central.add_vertex((365, 170))
    leg_central.add_vertex((377, 210))
    leg_central.add_vertex((400, 195))
    leg_central.add_vertex((395, 165))
    leg_central.filled = True
    leg_central.fill_color = 'white'
    leg_central.color = 'white'
    window.add(leg_central)

    leg_3 = GArc(200, 200, 370, 60)
    leg_3.color = 'white'
    window.add(leg_3, 351, 162)
    leg_4 = GArc(200, 200, 370, 60)
    leg_4.color = 'white'
    window.add(leg_4, 350, 162)
    leg_5 = GArc(200, 200, 370, 60)
    leg_5.color = 'white'
    window.add(leg_5, 349, 162)
    leg_6 = GArc(200, 200, 370, 60)
    leg_6.color = 'white'
    window.add(leg_6, 348, 162)
    leg_7 = GArc(200, 200, 370, 60)
    leg_7.color = 'white'
    window.add(leg_7, 347, 162)

    leg_8 = GRect(10, 10)
    leg_8.filled = True
    leg_8.fill_color = 'white'
    leg_8.color = 'white'
    window.add(leg_8, 386, 165)
    leg_9 = GRect(15, 15)
    leg_9.filled = True
    leg_9.fill_color = 'white'
    leg_9.color = 'white'
    window.add(leg_9, 386, 170)
    leg_10 = GRect(15, 20)
    leg_10.filled = True
    leg_10.fill_color = 'white'
    leg_10.color = 'white'
    window.add(leg_10, 390, 175)
    leg_11 = GRect(15, 20)
    leg_11.filled = True
    leg_11.fill_color = 'white'
    leg_11.color = 'white'
    window.add(leg_11, 395, 182)

    leg_down1 = GPolygon()
    leg_down1.add_vertex((377, 210))
    leg_down1.add_vertex((414, 194))
    leg_down1.add_vertex((415, 200))
    leg_down1.add_vertex((382, 215))
    leg_down1.filled = True
    leg_down1.fill_color = 'white'
    leg_down1.color = 'white'
    window.add(leg_down1)

    leg_triangle = GPolygon()
    leg_triangle.add_vertex((390, 220))
    leg_triangle.add_vertex((420, 208))
    leg_triangle.add_vertex((400, 196))
    leg_triangle.filled = True
    leg_triangle.fill_color = 'black'
    window.add(leg_triangle)

    left_knee = GOval(10, 10)
    left_knee.filled = True
    left_knee.fill_color = 'white'
    left_knee.color = 'white'
    window.add(left_knee, 383, 210)
    left_knee_1 = GArc(50, 50, 325, 60)
    left_knee_1.color = 'white'
    window.add(left_knee_1, 388, 203)

    left_leg = GPolygon()
    left_leg.add_vertex((385, 219))
    left_leg.add_vertex((384, 255))
    left_leg.add_vertex((388, 253))
    left_leg.add_vertex((393, 218))
    left_leg.filled = True
    left_leg.fill_color = 'white'
    left_leg.color = 'white'
    window.add(left_leg)

    right_leg = GPolygon()
    right_leg.add_vertex((410, 203))
    right_leg.add_vertex((411, 240))
    right_leg.add_vertex((415, 238))
    right_leg.add_vertex((417, 201))
    right_leg.filled = True
    right_leg.fill_color = 'white'
    right_leg.color = 'white'
    window.add(right_leg)

    fill_1 = GOval(20, 20)
    fill_1.filled = True
    fill_1.fill_color = 'white'
    fill_1.color = 'white'
    window.add(fill_1, 370, 160)
    fill_2 = GOval(10, 10)
    fill_2.filled = True
    fill_2.fill_color = 'white'
    fill_2.color = 'white'
    window.add(fill_2, 380, 200)
    fill_3 = GOval(10, 10)
    fill_3.filled = True
    fill_3.fill_color = 'white'
    fill_3.color = 'white'
    window.add(fill_3, 385, 197)
    fill_4 = GOval(9, 9)
    fill_4.filled = True
    fill_4.fill_color = 'white'
    fill_4.color = 'white'
    window.add(fill_4, 408, 194)
    fill_5 = GOval(7, 7)
    fill_5.filled = True
    fill_5.fill_color = 'white'
    fill_5.color = 'white'
    window.add(fill_5, 410, 192)

    right_knee_1 = GArc(50, 50, 355, 60)
    right_knee_1.color = 'white'
    window.add(right_knee_1, 406, 192)
    right_knee_2 = GArc(50, 50, 355, 60)
    right_knee_2.color = 'white'
    window.add(right_knee_2, 406, 192)
    right_knee_3 = GArc(50, 50, 355, 60)
    right_knee_3.color = 'white'
    window.add(right_knee_3, 406, 188)
    right_knee_3 = GArc(50, 50, 355, 60)
    right_knee_3.color = 'white'
    window.add(right_knee_3, 405, 187)

    left_shoe = GPolygon()
    left_shoe.add_vertex((384, 255))
    left_shoe.add_vertex((388, 265))
    left_shoe.add_vertex((395, 265))
    left_shoe.add_vertex((392, 263))
    left_shoe.add_vertex((388, 253))
    left_shoe.filled = True
    left_shoe.fill_color = 'white'
    left_shoe.color = 'white'
    window.add(left_shoe)

    right_shoe = GPolygon()
    right_shoe.add_vertex((411, 240))
    right_shoe.add_vertex((409, 245))
    right_shoe.add_vertex((425, 248))
    right_shoe.add_vertex((415, 243))
    right_shoe.add_vertex((415, 238))
    right_shoe.filled = True
    right_shoe.fill_color = 'white'
    right_shoe.color = 'white'
    window.add(right_shoe)

    floor = GLine(350, 300, 450, 300)
    floor.color = 'white'
    window.add(floor)

    paint_1 = GArc(100, 100, 360, 80)
    window.add(paint_1, 373, 170)
    paint_2 = GArc(100, 100, 360, 80)
    window.add(paint_2, 372, 170)
    paint_3 = GArc(100, 100, 360, 80)
    paint_3.color = 'white'
    window.add(paint_3, 374, 170)
    paint_4 = GArc(120, 120, 360, 75)
    window.add(paint_4, 370, 170)
    paint_4 = GArc(120, 120, 360, 75)
    window.add(paint_4, 369, 170)
    paint_5 = GLine(415, 200, 415, 220)
    window.add(paint_5)
    paint_6 = GLine(416, 200, 415, 220)
    window.add(paint_6)
    paint_7 = GLine(390, 222, 388, 242)
    window.add(paint_7)
    paint_8 = GLine(391, 222, 388, 242)
    window.add(paint_8)
    paint_9 = GLine(405, 180, 415, 200)
    window.add(paint_9)
    paint_10 = GLine(406, 180, 415, 200)
    window.add(paint_10)
    paint_11 = GLine(407, 180, 416, 200)
    window.add(paint_11)
    paint_12 = GLine(395, 170, 405, 180)
    window.add(paint_12)
    paint_13 = GLine(395, 170, 406, 180)
    window.add(paint_13)
    paint_14 = GLine(395, 170, 407, 180)
    window.add(paint_14)
    paint_15 = GLine(392, 135, 393, 160)
    window.add(paint_15)
    paint_16 = GArc(120, 120, 355, 70)
    window.add(paint_16, 360, 130)
    paint_17 = GArc(120, 120, 355, 70)
    window.add(paint_17, 359, 130)

    cloth = GLabel('24')
    cloth.font = 'Courier-12-Bold'
    window.add(cloth, 368, 158)

    title1 = GLabel('KOBE')
    title1.font = 'Times new roman-24-Bold'
    title1.color = 'orange'
    window.add(title1, 600, 140)
    title2 = GLabel('BRYANT')
    title2.font = 'Times new roman-24-Bold'
    title2.color = 'orange'
    window.add(title2, 585, 170)
    title3 = GLabel('THE')
    title3.font = 'Times new roman-12-Bold'
    title3.color = 'gray'
    window.add(title3, 623, 190)
    title4 = GLabel('MAMBA')
    title4.font = 'Times new roman-24-Bold'
    title4.color = 'gray'
    window.add(title4, 590, 220)
    title4 = GLabel('MENTALITY')
    title4.font = 'Times new roman-24-Bold'
    title4.color = 'gray'
    window.add(title4, 565, 250)
    honor = GLabel('5× NBA champion, 2× NBA Finals MVP, 1x MVP, 18× NBA All-Star, 4× NBA All-Star Game MVP')
    honor.font = 'Courier-12-Bold'
    honor.color = 'oldlace'
    window.add(honor, 80, 360)


if __name__ == '__main__':
    main()
