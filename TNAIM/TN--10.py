incomeTax:float = 0
salary:float = 0
while True:
    try:
        salary = float(input("please enter your salary"))
        if salary <= 6000:
            incomeTax = 0
        elif  6000 < salary <= 12000:
            incomeTax = (salary - 6000) / 10
        elif 12000 < salary <= 18000:
            incomeTax = (12000 - 6000) / 10 + (salary - 12000) * 0.2
        elif 18000 < salary <= 25000:
            incomeTax = (12000 - 6000) / 10 + (18000 - 12000) * 0.2 + (salary - 18000) * 0.3
        elif 25000 < salary <= 35000:
            incomeTax = (12000 - 6000) / 10 + (18000 - 12000) * 0.2 + (25000 - 18000) * 0.3 + (salary - 20000) * 0.4
        elif 35000 < salary <= 50000:
            incomeTax = (12000 - 6000) / 10 + (18000 - 12000) * 0.2 + (25000 - 18000) * 0.3 + (35000 - 20000) * 0.4 \
            + (salary - 35000) * 0.5
        else:
            if salary > 50000:
                incomeTax =    incomeTax = (12000 - 6000) / 10 + (18000 - 12000) * 0.2 + (25000 - 18000) * 0.3 + (35000 - 20000) * 0.4/\
            + (50000 - 35000) * 0.5 + (salary - 50000) * 0.51
        print(f"incometax is {incomeTax: .2f}")
        break
    except Exception as e:
        print("you entered a wrong salary")
        continue

#####################################
incomeTax2:float = 0
salary2:float = 0
while True:
    try:
        salary2 = float(input("please enter your salary"))
        match salary2:
            case slalary2 if salary2 <= 6000:
                incomeTax2 = 0
            case salary2 if  6000 < salary2 <= 12000:
                incomeTax2 = (salary - 6000) / 10
            case salary2 if 12000 < salary2 <= 18000:
                incomeTax2 = (12000 - 6000) / 10 + (salary2 - 12000) * 0.2
            case salary2 if 18000 < salary2 <= 25000:
                incomeTax2 = (12000 - 6000) / 10 + (18000 - 12000) * 0.2 + (salary2 - 18000) * 0.3
            case salary2 if 25000 < salary2 <= 35000:
                incomeTax2 = (12000 - 6000) / 10 + (18000 - 12000) * 0.2 + (25000 - 18000) * 0.3 + (salary2 - 20000) * 0.4
            case salary2 if 35000 < salary2 <= 50000:
                incomeTax2 = (12000 - 6000) / 10 + (18000 - 12000) * 0.2 + (25000 - 18000) * 0.3 + (35000 - 20000) * 0.4 \
                + (salary2 - 35000) * 0.5
            case salary2  if salary2 > 50000:
                    incomeTax2 =    incomeTax = (12000 - 6000) / 10 + (18000 - 12000) * 0.2 + (25000 - 18000) * 0.3 + (35000 - 20000) * 0.4/\
                + (50000 - 35000) * 0.5 + (salary2 - 50000) * 0.51
        print(f"incometax is {incomeTax2: .2f}")
        break
    except Exception as e:
        print("you entered a wrong salary {e}")
        continue






