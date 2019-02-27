print('Can String Be Float')
def main():
    user_value = input('Enter a value:')
    try:
        float(user_value)
        print(float(user_value), 'is float')
        print('True')
    except:
        print('False')
        return main()
main()
