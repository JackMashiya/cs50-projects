def main():
    user = input('What time is it? ').strip()
    timeHrs = convert(user)

    if 7.0 <= timeHrs <= 8.0:
        print('breakfast time')
    elif 12.0 <= timeHrs <= 13.0:
        print('lunch time')
    elif 18.0 <= timeHrs <= 19.0:
        print('dinner time')



def convert(time):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)
    return hours + (minutes / 60)

    
if __name__ == "__main__":
    main()
