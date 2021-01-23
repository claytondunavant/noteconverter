from pdf2image import convert_from_path
from os import system

class Slides2Notes:

    numSlides = 0

    def slides2images(self):
        imgsDir = self.processID + "/imgs"
        system("mkdir " + imgsDir)

        images = convert_from_path(self.input)

        for image in images:
            image.save(imgsDir + "/slide" + str(self.numSlides) + ".jpg", 'JPEG')
            self.numSlides = self.numSlides + 1


    def run(self):
        # create file for current id
        system("mkdir " + self.processID)

        #turn the slides into images        
        self.slides2images()

        # delete current id file
        # system("rm -rf " + str(self.numId))

    def __init__(self, processID, input, outputType):
        self.processID = str(processID)
        self.input = input
        self.outputType = outputType
        self.run()

    
