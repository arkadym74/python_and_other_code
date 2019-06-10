inputFile = open('myimage.jpg', 'rb')
outputFile = open('myoutputimage.jpg', 'wb')

msg = inputFile.read()
outputFile.write(msg)


inputFile.close()
outputFile.close()
