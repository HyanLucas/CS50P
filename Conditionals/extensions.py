def main():
    file = str(input("File name: "))
    print(find_type(file))


def find_type(file):
    file_type = file.split(".")[1]
    match file_type:
        case "gif":
            return "image/gif"
        case "jpg":
            return "image/jpeg"
        case "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


main()
