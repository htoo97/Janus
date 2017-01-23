import cv2, sys, smtplib

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

DEVICE_NUMBER = 0
IMAGE_FILE = "email_attachment.jpg"

if len(sys.argv) > 1:
        XML_PATH = sys.argv[1]
else:
        print "Error: XML path not defined"
        sys.exit(1)

faceCascade = cv2.CascadeClassifier(XML_PATH)

vc = cv2.VideoCapture(DEVICE_NUMBER)

if vc.isOpened():
	retval, frame = vc.read()
else:
	sys.exit(1)

i = 0
faces = []

while retval:
	frame_show = frame
	
	if i%5 == 0:
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		faces = faceCascade.detectMultiScale(
			frame,
			scaleFactor=1.3,
			minNeighbors=2,
			minSize=(50,50),
			flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		)


	if len(faces) > 0:	
		faceNum = 0
		for (x,y,w,h) in faces:
			faceNum+= 1
			cv2.rectangle(frame_show, (x,y), (x+w, y+h), (0,0,255), 2)
			processed_img = frame[y:y+h, x:x+w]
			cv2.equalizeHist(processed_img, processed_img)
			IMAGE_FILE = "email_attachment.jpg"
			
			cv2.imwrite(IMAGE_FILE, frame_show)

      # cropped, greyscale and histogram-adjusted picture
      # potentially to be used for training facial recognition
			cv2.imwrite("detected_face.jpg", processed_img)
    
    EMAIL_ADDRESS = "enter_your_@_email_address.com"
    EMAIL_USERNAME = "your_username"
    EMAIL_PASSWORD = "your_password"

    # Use link below to find out your carrier's email address
    # http://www.digitaltrends.com/mobile/how-to-send-e-mail-to-sms-text/
    PHONE_ADDRESS = "your_phone_number_@_your_carrier.site" 

    msg = MIMEMultipart()
    msg.attach(MIMEText("Face detected!"))
    msg['Subject'] = "DragonBoard Camera triggered!"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = PHONE_ADDRESS

    try:
	    f = open(IMAGE_FILE, "rb")
    	img = MIMEImage( f.read() )
	    f.close()
	    msg.attach(img)
    except IOError:
	    print "Error: Cannot find"

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(EMAIL_USERNAME,EMAIL_PASSWORD)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.quit()

		import send_sms		
		break
 
	cv2.imshow("Detecting Faces", frame_show)

	retval, frame = vc.read()

	if cv2.waitKey(1) == 27:
		break

	i += 1


