import cv2
import pytesseract
import numpy as np
import os



def OCR():
    #initialisation
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

    percentage=25
    roi=[[(18, 194), (220, 226), ' text', ' Name'],
        [(22, 270), (222, 302), ' text', ' Phone'],
        [(20, 340), (220, 376), ' text', ' Email'],
        [(22, 416), (220, 448), ' text', ' Adhaar']]


    imgM=cv2.imread('main_template.jpg')
    h,w,c=imgM.shape

    #check for keypoints
    orb =cv2.ORB_create(1000)
    kp1, des1 = orb.detectAndCompute(imgM,None)
    #impKp1= cv2.drawKeypoints(imgM,kp1,None)
    #mapping
    imgpath='Details'
    img_details=os.listdir(imgpath)
    #{print(img_details)}
    for x,y in enumerate(img_details):
        file_path=imgpath + "/"+y
        img=cv2.imread(file_path)
        print(file_path)
        print(os.path.exists(file_path))
        #cv2.imshow(y,img)
        kp2, des2 = orb.detectAndCompute(img,None)
        
    #Matcher
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        matches=bf.match(des2,des1)
        matches.sort(key=lambda x: x.distance) #lower the distance better the accuracy
        good = matches[:int(len(matches)*(percentage/100))]   
        
    #draw
        imgMatch=cv2.drawMatches(img,kp2,imgM,kp1,good[0:100],None,flags=2)
        #cv2.imshow(y,imgMatch)
        
        srcPoints= np.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1,1,2)       
        desPoints= np.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1,1,2)
        
        M, _ = cv2.findHomography(srcPoints,desPoints,cv2.RANSAC,5.0)
        imgScan = cv2.warpPerspective(img,M,(w,h))
        #imgScan=cv2.resize(imgScan,(w//5,h//5))
        #cv2.imshow(y,imgScan)
        
        imgShow = imgScan.copy()
        imgMask= np.zeros_like(imgShow) 

        data=[]
        print(f'######Extracting Data from Form - {x+1}##############')
        for x,r in enumerate(roi):
            cv2.rectangle(imgMask,(r[0][0],r[0][1]),(r[1][0],r[1][1]),(0,255,0),cv2.FILLED)
            imgShow=cv2.addWeighted(imgShow,0.99,imgMask,0.1,0) 
            
            imgCrop= imgScan[r[0][1]:r[1][1], r[0][0]:r[1][0]]
            #cv2.imshow(str(x), imgCrop)
            
            if r[2] == ' text':
                print(f'{r[3]}:{pytesseract.image_to_string(imgCrop)}')
                data.append(pytesseract.image_to_string(imgCrop))
                
                
            cv2.putText(imgShow,str(data[x]),(r[0][0],r[0][1]),cv2.FONT_HERSHEY_PLAIN ,1.5,(0,0,255),2)    
                
        for i in range(len(data)):
            data[i] = data[i].replace("\n\x0c", "")        
        
        with open('data.csv','a+') as f:
            for d in data:
                f.write((str(d)+','))
            f.write('\n')
                
        
        #print(data)
        
        
        #cv2.imshow(y+"2",imgShow)
        cv2.imwrite("output/" + y,imgShow)     
        
        

        

    # #cv2.imshow("output",imgM)
    cv2.waitKey(0)