#FAT FREE MASS INDEX
kilo_weight=float(input('Enter weight in kilos'))
metre_height=float(input('Enter height in meters'))
body_fat=float(input('Enter body-fat percentage'))
def total_body_fat():
    global kilo_weight
    global metre_height
    global body_fat
    return kilo_weight * (body_fat/100)
def lean_weight():
    global kilo_weight
    global metre_height
    global body_fat
    return kilo_weight *(1-(body_fat/100))
def inches_to_metres(inches):
    return inches*0.0254
def ffmi():
    global metre_height
    feet,inches=map(float,input('Enter height in feet and inches').split())
    return (lean_weight() / 2.2)/((feet*12+inches)*0.0254)**2

    
