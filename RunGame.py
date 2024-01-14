import os
import pyautogui
import time

def holdKey(key, seconds=1.00):
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key)

#atveram aplikaciju
os.startfile(r"C:\Users\geeze\AppData\Local\Programs\y8-browser\Y8 Browser.exe")
time.sleep(3)

#atrodam mekletaja pogu un ierakstam speles nosaukumu
search = pyautogui.locateCenterOnScreen("imagesForBot\\BotSearchGame.png", confidence=0.9)
pyautogui.moveTo(*search, 0.5)
pyautogui.click()
game_name = 'Sinjid'
pyautogui.write(game_name)
pyautogui.hotkey('enter')

#atveram speli
time.sleep(1)
open_game = pyautogui.locateCenterOnScreen("imagesForBot\\GameItself.png", confidence=0.7)
pyautogui.moveTo(*open_game, 0.5)
pyautogui.click()

#nospiezam pirmo pogu
time.sleep(1)
play_button = pyautogui.locateCenterOnScreen("imagesForBot\\play_button.png", confidence=0.9)
pyautogui.moveTo(*play_button, 0.5)
pyautogui.click()

#nospiezam otro pogu
time.sleep(2)
real_play_button = pyautogui.locateCenterOnScreen("imagesForBot\\play_button1.png", confidence=0.7)
pyautogui.moveTo(*real_play_button, 0.5)
pyautogui.click()

#nospiezam skip pogu
time.sleep(1)
skip_button = pyautogui.locateCenterOnScreen("imagesForBot\\skip_button.png", confidence=0.7)
pyautogui.moveTo(*skip_button, 0.5)
pyautogui.click()

#nospiezam skip pogu
time.sleep(1)
start_button = pyautogui.locateCenterOnScreen("imagesForBot\\start_button.png", confidence=0.7)
pyautogui.moveTo(*start_button, 0.5)
pyautogui.click()

#nospiezam proceed pogu
time.sleep(1)
proceed_button = pyautogui.locateCenterOnScreen("imagesForBot\\proceed_button.png", confidence=0.7)
pyautogui.moveTo(*proceed_button, 0.5)
pyautogui.click()

#izvelamies par ko spelet
time.sleep(1)
warrior = pyautogui.locateCenterOnScreen("imagesForBot\\warrior.png", confidence=0.7)
pyautogui.moveTo(*warrior, 0.5)
pyautogui.click()
time.sleep(1)

#sakam noradit kurus taustinus vajag turet lai aizietu uz mums vajadzigo lokaciju
#istaba 1
holdKey('w', 1)
pyautogui.press('space')
#istaba 2
holdKey('d', 2.5)
pyautogui.press('space')
#istaba 3
holdKey('d', 2.75)
holdKey('w', 1)
pyautogui.press('space')
#istaba 4
holdKey('a', 3)
pyautogui.press('space')
#istaba 5
holdKey('a', 1.8)
holdKey('w', 1)
pyautogui.press('space')
#istaba 6
holdKey('a', 2)
pyautogui.press('space')
#istaba 7
holdKey('a', 1.5)
holdKey('w', 0.25)
holdKey('a', 0.25)
pyautogui.press('space')
pyautogui.press('space')
holdKey('d', 2)
pyautogui.press('space')
#atkal istaba 6
holdKey('w', 0.5)
holdKey('d', 2.5)
pyautogui.press('space')
pyautogui.press('space')
holdKey('d', 1)
pyautogui.press('space')
#gala istaba
holdKey('d', 0.75)
pyautogui.press('space')
training_start = (982, 314)
pyautogui.click(training_start)
time.sleep(4)

#kauja 1
def perform_action(image_path, confidence=0.8):
    time.sleep(4.5)
    try:
        action_button = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if action_button is not None:
            pyautogui.moveTo(*action_button, 0.5)
            pyautogui.click()
        else:
            print("Error: Bilde nav atrasta, skipojam...")
    except pyautogui.ImageNotFoundException:
        print("Error: Bilde nav atrasta, skipojam...")
# stiprais sitiens
for i in range(1, 5):
    time.sleep(1)
    perform_action("imagesForBot\\strong_attack.png")
# parasts uzbrukums
for i in range(1, 11):
    perform_action("imagesForBot\\uzbrukums.png")
# izdzeram veselibas dzirinu
perform_action("imagesForBot\\health5.png")
# turpinam parastos uzbrukumus
for i in range(1, 14):
    perform_action("imagesForBot\\uzbrukums.png")

#laiks dabut limeni
time.sleep(1)
continue_button = pyautogui.locateCenterOnScreen("imagesForBot\\continue_button.png", confidence=0.7)
pyautogui.moveTo(*continue_button, 0.5)
pyautogui.click()
time.sleep(1)
strenght_skill = pyautogui.locateCenterOnScreen("imagesForBot\\strenght_skill.png", confidence=0.7)
pyautogui.moveTo(*strenght_skill, 0.5)
pyautogui.click()
time.sleep(1)
continue_button = pyautogui.locateCenterOnScreen("imagesForBot\\continue_button.png", confidence=0.7)
pyautogui.moveTo(*continue_button, 0.5)
pyautogui.click()
time.sleep(1)
skillpoint1 = pyautogui.locateCenterOnScreen("imagesForBot\\skillpoint1.png", confidence=0.7)
pyautogui.moveTo(*skillpoint1, 0.5)
pyautogui.click()
time.sleep(1)
skillpoint2 = pyautogui.locateCenterOnScreen("imagesForBot\\skillpoint2.png", confidence=0.7)
pyautogui.moveTo(*skillpoint2, 0.5)
pyautogui.click()
time.sleep(1)
continue_button = pyautogui.locateCenterOnScreen("imagesForBot\\continue_button.png", confidence=0.7)
pyautogui.moveTo(*continue_button, 0.5)
pyautogui.click()
time.sleep(1)

#kauja 2
pyautogui.press('space')
training_start = (982, 314)
pyautogui.click(training_start)
time.sleep(4)
# stiprais sitiens
for i in range(1, 5):
    time.sleep(1)
    perform_action("imagesForBot\\strong_attack.png")
# parasts uzbrukums
for i in range(1, 11):
    perform_action("imagesForBot\\uzbrukums.png")
# izdzeram veselibas dzirinu
perform_action("imagesForBot\\health5.png")
# turpinam parastos uzbrukumus
for i in range(1, 14):
    perform_action("imagesForBot\\uzbrukums.png")
continue_button = pyautogui.locateCenterOnScreen("imagesForBot\\continue_button.png", confidence=0.7)
pyautogui.moveTo(*continue_button, 0.5)
pyautogui.click()
time.sleep(1)
#kauja 3
pyautogui.press('space')
training_start = (982, 314)
pyautogui.click(training_start)
time.sleep(4)
# stiprais sitiens
for i in range(1, 5):
    time.sleep(1)
    perform_action("imagesForBot\\strong_attack.png")
# parasts uzbrukums
for i in range(1, 11):
    perform_action("imagesForBot\\uzbrukums.png")
# izdzeram veselibas dzirinu
perform_action("imagesForBot\\health5.png")
# turpinam parastos uzbrukumus
for i in range(1, 14):
    perform_action("imagesForBot\\uzbrukums.png")
continue_button = pyautogui.locateCenterOnScreen("imagesForBot\\continue_button.png", confidence=0.7)
pyautogui.moveTo(*continue_button, 0.5)
pyautogui.click()


