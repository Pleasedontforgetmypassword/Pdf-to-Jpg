from pdf2image import convert_from_path
from sys import argv

def main():

    #declare name variable with the second control line argument to the last
    name = ' '.join(argv[1:len(argv)])

    try:

        #Opens image and saves it in variable images
        images = convert_from_path(f"./Input/{name}.pdf")

        #file count
        filecount = 0

        #loops over the pages
        for img in images:

            #convert the pages in Output Folder
            img.save(f"./Output/{name}-{filecount}.jpg", 'JPEG')

            #Tells the user what is going on
            print(f"Converting {name} to {name}-{filecount}.jpg. {name}-{filecount}.jpg Saved in Output Folder")

            #increases file count
            filecount += 1

        #after looping through the pages, Print Done
        print("Done")

        #returns 0 to indicate Success
        return 0

    except:

        #if error occurs then Tell the user
        print(f"Could not open {name}")

        #return 1 to indicate an error happened
        return 1

if __name__ == '__main__':
    main()