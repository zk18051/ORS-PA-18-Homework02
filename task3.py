print('Cube Volume')
def main():
    cube_lenght = input('Enter a cube lenght:')
    try:
        float(cube_lenght)
        if float(cube_lenght) < 0:
            print('-1')
            return main()
        else:
            print(cube_lenght)
    except:
        print('-1')
        return main()

    cube_volume = float(cube_lenght)**3
    print('Cube volume is', cube_volume)


main()
