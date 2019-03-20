def metric_bmi():
    weight=float(input('Enter weight in KG!'))
    height=float(input('Enter height in metres'))
    bmi=weight/(height**2)
    return bmi
def imperial_bmi():
    weight=float(input('Enter weight in pounds(lb)!'))
    height=float(input('Enter height in inches(in)'))
    bmi=weight/(height**2)*703
    return bmi
def kg_to_pounds(weight):
    return weight*2.20462
def pounds_to_kg(weight):
    return weight/2.20462
def metres_to_inches(x):
    return x*39.3701
def inches_to_metres(x):
    return x*0.0254
def bmi_result(bmi):
    if bmi < 15:
        return 'Very Severly Underweight'
    elif bmi < 16 and bmi >= 15:
        return 'Severly Underweight'
    elif bmi >=16 and bmi < 18.5:
        return 'UnderWeight'
    elif bmi >=18.5 and bmi < 25:
        return 'Normal Weight'
    elif bmi >= 25 and bmi < 30:
        return 'OverWeight'
    elif bmi >= 30 and bmi < 35:
        return 'Moderlately obese'
    elif bmi <= 35 and bmi < 40:
        return 'Severely obese'
    else:
        return 'Very Severly Obese'

