import pyttsx3
motor_audio = pyttsx3.init() #creamos el objeto para programarlo



# """ RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 125)     # setting up new voice rate

motor_audio.setProperty('rate', 90) #con esto podemos cambiar la velocidad a la que habla el objeto

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

voz_motor = motor_audio.getProperty('voices')

motor_audio.setProperty('voice', 'spanish')
motor_audio.setProperty('voice', voz_motor[0].id)

motor_audio.say('Hola como estas mi nombre es Priscila y tengo hambre quiero licuado')
motor_audio.runAndWait()
motor_audio.stop()