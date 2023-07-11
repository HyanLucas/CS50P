def convert(faces: str):
    faces = faces.replace(":)", '🙂') and faces.replace(":(", '🙁')
    return faces


def main():
    faces = str(input())
    faces = convert(faces)
    print(faces)


main()