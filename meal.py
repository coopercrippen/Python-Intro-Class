#Tells you what meal to eat at what time
def main():
    print(convert(input("What time is it? ")))

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time = hours + minutes / 60
    print(time)

    if 7 <= time <= 8:
        return("It is breakfast time.")
    elif 12 <= time <= 13:
        return("It is lunch time.")
    elif 17 <= time <= 20:
        return("It is dinner time.")
    else:
        return("You shouldn't be eating!")


if __name__ == "__main__":
    main()
