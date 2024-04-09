import MyModule as shapes

def main():
    try:
        y = shapes.triangle(2,3,5)
    except shapes.NieTrojkat as e:
        print(e.message)
    else:
        y.pole()
        y.obwod()
    x = shapes.circle(2)
    x.obwod()
    x.pole()

    z = shapes.square(2)
    z.obwod()
    z.pole()


if __name__ == "__main__":
    main()