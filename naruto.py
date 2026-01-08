import pyautogui
import pyperclip
import time
from mistral_ai import mistralai
import keyboard
import sys


api_key="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"
last_roasted=""

# Step 1: Wait to prepare
time.sleep(1)

# Step 2: Click icon (optional)
pyautogui.moveTo(652, 1064)
pyautogui.click()

# Step 3: Give browser time to load chat
time.sleep(2) 
while True:

  if keyboard.is_pressed('esc'):
     print("👋 Naruto Bot stopped by user.")
     sys.exit()


      
# Step 4: Move to chat start and pause
  pyautogui.moveTo(640, 157)
  pyautogui.click()
  time.sleep(1)
  
  # Step 5: Hold mouse and drag SLOWLY like a human
  pyautogui.mouseDown()
  pyautogui.moveTo(640,350, duration=1)  # smaller drag first — test this
  pyautogui.moveTo(640,750, duration=1)
  pyautogui.moveTo(640,1018, duration=1)
  pyautogui.mouseUp()
  
  # Step 6: Copy
  time.sleep(1)
  pyautogui.hotkey("ctrl", "c")
  time.sleep(1)
  pyautogui.click(1008,918)
  
  # Step 7: Get chat
  chat_history = pyperclip.paste()
  
  # 1. Split the messages (every line is a message)
  lines = chat_history.strip().split('\n')
  
  # 2. Get the last non-empty line
  last_line = None
  for line in reversed(lines):
       if line.strip():  # Skip empty lines
        last_line = line
        break

# 3. Check if the last line is from Rohan Das
  if last_line and "Bro:" in last_line  and last_line!=last_roasted:
       print("✅ Last message is from Bro. Generating roast...")
       response = mistralai(chat_history, api_key)
       print("Naruto Bot:", response)


    #sending roast to sender 
       pyperclip.copy(response)    
       time.sleep(1)
        
       pyautogui.moveTo(740,1000)
       pyautogui.click()
        
       pyautogui.hotkey("ctrl","v")
       time.sleep(1)
       pyautogui.press("Enter")

       last_roasted=last_line

  else:
       print("Nothing to roast for")

  time.sleep(5)