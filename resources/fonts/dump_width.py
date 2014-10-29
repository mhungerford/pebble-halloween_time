import os, sys
import fontforge

def main():

    # arguments, print an example of correct usage.
    if len(sys.argv) - 1 != 1:
        print("********************")
        print("Usage suggestion:")
        print("python " + sys.argv[0] + " <font.ttf>")
        print("********************")
        exit()

    input_filename = sys.argv[1]

    ff = fontforge.open(input_filename)
    for i in ff.selection.all():
        try:
            name, width = ff[i].glyphname, ff[i].width
            print i, name, width
        except:
            pass
        
if __name__ == '__main__':
    main()
