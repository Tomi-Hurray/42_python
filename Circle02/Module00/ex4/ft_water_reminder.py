def ft_water_reminder():
    days_s_w = int(input("Days since last watering: "))
    if days_s_w > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
