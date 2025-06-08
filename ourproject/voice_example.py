from gtts import gTTS
import pygame
pygame.mixer.init()
sound_file = "sound_file.mp3"
text_to_speech = gTTS(text='ကခဂ', lang='my')
text_to_speech.save(sound_file)
sound = pygame.mixer.Sound(sound_file)
sound.play()
while pygame.mixer.get_busy(): 
    pygame.time.delay(100)