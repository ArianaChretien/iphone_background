def setup():
    size(500, 500)
    noStroke()
    x = 0
    img = loadImage("classof2018.jpg")
    # txt = text("CLASS")
    while x < 500:
        y = 0
        while y < 500:
            # if x % 200 == 0:
            #     else: 
                # fill(0, 0, 0)
           image(img, x, y, 100, 100)
        # if y % 300 == 0:
        #         fill(255, 255, 255)
        #         rect(x, y, 10, 10)
           y = y + 100
        x = x + 100
        textSize(100)
        # translate( txt, 100, 2)
        # rotate(PI/3.0)
        text("CLASS", 50, 80)
