from pdf2image import convert_from_path
from sys import argv

def main():
    # make sure there is 2 command line argument
    if len(argv) != 2:

        #Tells the user To provide 2 command line arguments
        print("Failed to provide 2 command line arguments.")

        #returns 1 to indicate a error
        return 1

    try:

        #Opens image and saves it in variable images
        images = convert_from_path(f"./Input/{argv[1]}.pdf")

        #file count
        filecount = 0

        #loops over the pages
        for img in images:

            #convert the pages in Output Folder
            img.save(f"./Output/{argv[1]}-{filecount}.jpg", 'JPEG')

            #Tells the user what is going on
            print(f"Converting {argv[1]} to {argv[1]}-{filecount}.jpg. {argv[1]}-{filecount}.jpg Saved in Output Folder")

            #increases file count
            filecount += 1

        #after looping through the pages, Print Done
        print("Done")

        #returns 0 to indicate Success
        return 0

    except:

        #if error occurs then Tell the user
        print(f"Could not open {argv[1]}")

        #return 1 to indicate an error happened
        return 1

if __name__ == '__main__':
    main()