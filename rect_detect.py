import cv2
import numpy as np
import imutils

font = cv2.FONT_HERSHEY_COMPLEX 
img2 = cv2.imread('p1.jpg', cv2.IMREAD_COLOR)

img = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img2=imutils.resize(img2,width=800)
img=imutils.resize(img,width=800)
cv2.imshow('gri',img)

_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY) #Piksel değerleri için belirli bir eşik (threshold) değeri için alt 0 ve üst 255 olacak Binary transformasyonu
contours, hi= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #cv2 içinde bulunan Kontor bulmak için kullandığım fonksiyon. cv2.CHAIN_APPROX_NONE kullanılarak
                                                                                #sadece bütün kontor çizgisi yerine çizgilerin başlangıç ve bitiş koordinatları elde edilir.
cv2.imshow('thresh',threshold) #Threshold uygulanmış resmin gösterimi
for cnt in contours : 
  
    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)      # numpy array'i cinsinden kontorların alınması
    alan=cv2.contourArea(cnt) #Kontor alanı
    if alan > 200 and alan < 3000 :       # Alan parametreleri, fotoğrafın çekildiği yüksekliğe göre değişiyor. 
                                          # Aynı yukseklikten cekilmiş olan fotograflar icin sabit degerler kullanilabilir.
        cevre= cv2.arcLength(cnt,True)    
        print('Alan: ',alan, '  cevre: ',cevre)
        x,y,w,h = cv2.boundingRect(cnt)
        fark=int(w-h)
        
        if abs(fark) <100: # -- Elde edilen dörgenlerden kareye en yakın olanı çizdirmek için genişlik ve yükseklik değeri farkı eldesi.
         cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2) # kontor dortgeni
         cv2.rectangle(img2,(x+int(w/4),y+int(h/4)) , (x+w-int(w/4), y+h-int(h/4)), (255,0,0), 1) #muhtemel harf bolgesi (2x2'lik posterde 1x1'lik harf bölgesi)
         #cv2.drawContours(img, [approx], 0, (0, 0, 255), 5) #İşlenmiş resimden elde edilen kontorların en başta import ettiğimiz işlenmemiş renkli fotoğraf üzerine çizilmesi
         print('x:',x,' y:',y,' en:',w,' boy:',h)
         
cv2.imshow('kontorlar', img2) #İşlenmiş resimden elde edilen kontorların en başta import ettiğimiz işlenmemiş renkli fotoğraf üzerine çizilmesi
cv2.waitKey(0)
