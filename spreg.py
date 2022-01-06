import speech_recognition as sr
import pyttsx3
import pyautogui as pg
import webbrowser
import time
 


r = sr.Recognizer() 
pg.FAILSAFE=False


def fun(function, args):
    function(*args)

def SpeakText(command):
      
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
      
##def spk(z):
####    global c
##    try:
##        
##        with sr.Microphone() as source2:
##            r.adjust_for_ambient_noise(source2, duration=0.2)
##              
##            #listens for the user's input 
##            audio2 = r.listen(source2)
##            
##              
##            # Using ggogle to recognize audio
##            Mytext = r.recognize_google(audio2)
##            Mytext = Mytext.lower()
##            q=Mytext
##            q=str(q)
####            c.insert(0,q)
##            
##            webbrowser.open('https://www.youtube.com/search?q='+q)
##            
##            
##                
##    except sr.RequestError as e:
##        print("Could not request results; {0}".format(e))
##          
##    except sr.UnknownValueError:
##        print("unknown error occured")
##    except KeyError:
##        print('key')


def spk1(z):
##    global d
    try:
        
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
              
            #listens for the user's input 
            audio2 = r.listen(source2)
            
              
            # Using ggogle to recognize audio
            myText = r.recognize_google(audio2)
            myText = myText.lower()
            d=myText
            pg.typewrite(d)
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")
    except KeyError:
        print('key')
    

b=list(pg.size())
x=b[0]/3
y=b[1]/3
tl=(x/2,y/2)
tm=(x+tl[0],tl[1])
tr=(x+tm[0],tm[1])
ml=(tl[0],tl[1]+y)
mm=(tm[0],ml[1])
mr=(x+mm[0],mm[1])
bl=(tl[0],ml[1]+y)
bm=(tm[0],mm[1]+y)
br=(tr[0],mm[1]+y)
##print(c)
a='' 

 
 
v=''
l=['youtube voice search','typing','move to tab','shift','swift']
while(1):    
      

     
    try:
          
        # use the microphone as source for input.
        with sr.Microphone() as source2:
              
             
            r.adjust_for_ambient_noise(source2, duration=0.2)
              
            #listens for the user's input 
            audio2 = r.listen(source2)
              
            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            a=MyText
            print(a)
            a=str(a)
            v=a
            d={'top left':[(pg.moveTo,(tl,))],'top middle':[(pg.moveTo,(tm,))],'top right':[(pg.moveTo,(tr,))],
                      'middle left':[(pg.moveTo,(ml,))],'middle middle':[(pg.moveTo,(mm,))],'middle right':[(pg.moveTo,(mr,))],
                      'bottom left':[(pg.moveTo,(bl,))],'bottom middle':[(pg.moveTo,(bm,))],'bottom right':[(pg.moveTo,(br,))],
                      'google voice search':[(webbrowser.open,('https://www.google.com',)),(time.sleep,(2,)),(pg.hotkey,("ctrlleft","shift","."))],
                      'youtube voice search' in a:lambda :[(webbrowser.open,('https://www.youtube.com/search?q='+a[21:],))],
                      'click':[(pg.click,(None, None, 1, 0.0, "left"))],
                      'close this tab':[(pg.hotkey,('ctrlleft','w'))],
                      'right click':[(pg.click,(None, None, 1, 0.0, "right"))],'open new tab':[(pg.hotkey,('ctrlleft','t'))],
                      'close application':[(pg.hotkey,('alt','F4'))],'left':[(pg.move,(-50,0))],'right':[(pg.move,(50,0))],
                      'upside':[(pg.move,(0,-50))],'down':[(pg.move,(0,50))],
                      'open cmd':[(pg.hotkey,('winleft',)),(time.sleep,(1,)),(pg.typewrite,('cmd',)),(time.sleep,(1,)),(pg.hotkey,('enter',))],
                      'typing' in a:lambda:[(pg.typewrite,(a[7:],))],'whatsapp web':[(webbrowser.open,('web.whatsapp.com',))],
                      'minimise all windows':[(pg.hotkey,('winleft','m'))],
                      'minimise this window':[(pg.hotkey,('alt','space')),(time.sleep,(2,)),(pg.hotkey,('enter',))],
                      'send a whatsapp message':[(pg.hotkey,('ctrl','alt','/')),(time.sleep,(1,)),(spk1,('h',)),(time.sleep,(1,)),
                                                  (pg.hotkey,('enter',)),(time.sleep,(1,)),(spk1,('h',)),(time.sleep,(1,)),(pg.hotkey,('enter',))],
                      'open notepad':[(pg.hotkey,('winleft',)),(time.sleep,(1,)),(pg.typewrite,('notepad',)),(time.sleep(1,)),(pg.hotkey,('enter',))],
                      'caps lock':[(pg.hotkey,('capslock',))],
                      'space':[(pg.hotkey,('space',))],
                      'pause video':[(pg.hotkey,('space',))],
                      'double click':[(pg.click,(None, None, 1, 0.0, "left")),(pg.click,(None, None, 1, 0.0, "right"))],
                      'scroll down':[(pg.scroll,(-7,))],'scroll up':[(pg.scroll,(7,))],
                      'comma':[(pg.hotkey,(',',))],
                      'capital' in a:lambda:[(pg.hotkey,('capslock',)),(pg.typewrite,(a[8:],))],
                      'back space':[(pg.hotkey,('backspace',))],
                      'enter':[(pg.hotkey,('enter',))],'full stop':[(pg.hotkey,('.',))],
                      'move to tab' in a:lambda:[(pg.hotkey,('ctrlleft',a[12:]))],
                      'swift' in a:lambda:[(pg.hotkey,('shift',a[6:]))],
                      'round bracket':[(pg.hotkey,('()',))],'square bracket':[(pg.hotkey,('[]',))],
                      'curly bracket':[(pg.hotkey,('{}',))],'semicolon':[(pg.hotkey,(';',))],'colon':[(pg.hotkey,(':',))],
                      'windows':[(pg.hotkey,('winleft',))],'arrow up':[(pg.hotkey,('up',))],'arrow down':[(pg.hotkey,('down',))],
                      'arrow left':[(pg.hotkey,('left',))],'arrow right':[(pg.hotkey,('right',))]
                      }
##            for i in l:
##                if i in a:
            try:

                for i in d[True]():
                    fun(i[0],i[1])
                
            except KeyError:
                
                if v=='stop the application':
                    while(v!='start the application'):
                        try:
                            with sr.Microphone() as source2:
                                r.adjust_for_ambient_noise(source2, duration=0.2)
                                audio2 = r.listen(source2)
                                MyTexT = r.recognize_google(audio2)
                                MyTexT = MyTexT.lower()
                                v=MyTexT
                                print(v)
                        except sr.RequestError as e:
                            print("Could not request results; {0}".format(e))
              
                        except sr.UnknownValueError:
                            print("unknown error occured")
                        except KeyError:
                            print('key')
                
                for i in d[a]:
                    fun(i[0],i[1])
                
                
                    
            
 
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        SpeakText('try again')
        print("unknown error occured")
    except KeyError:
        SpeakText('key error')
        print('key')
##    except TypeError:
##        print('type')
 
