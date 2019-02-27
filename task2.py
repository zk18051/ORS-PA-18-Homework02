print('Convert Kilometers To Miles')
def main():
    user_value = input('Enter kilometers:')
    try:
        float(user_value)
        print(float(user_value),'km')
    except:
        print(user_value, 'is not a number. Try again.')
        return main()
    user_miles = float(user_value) * 0.62137
    print(user_value, 'km is', user_miles, 'miles')

main()