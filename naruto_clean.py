import pyautogui
import pyperclip
import time
from mistral_ai import mistralai
import keyboard

api_key = "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"
last_roasted = ""

# Step 1: Wait to prepare
time.sleep(1)

# Step 2: Click icon (optional)
pyautogui.moveTo(652, 1064)
pyautogui.click()

# Step 3: Give browser time to load chat
time.sleep(2)

print("🤖 Naruto Bot is now running. Press ESC to stop.")

while True:
    if keyboard.is_pressed('esc'):
        print("👋 Naruto Bot stopped by user.")
        break

    # Step 4: Move to chat start and pause
    pyautogui.moveTo(635, 200)
    time.sleep(0.3)

    # Step 5: Drag chat slowly
    pyautogui.mouseDown()
    pyautogui.moveTo(635, 350, duration=1)
    pyautogui.moveTo(635, 750, duration=1)
    pyautogui.moveTo(635, 1018, duration=1)
    pyautogui.mouseUp()

    # Step 6: Copy selected chat
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(3)
    pyautogui.click(1008, 918)  # refocus chat window

    # Step 7: Get chat
    chat_history = pyperclip.paste()
    lines = chat_history.strip().split('\n')

    # Step 8: Get last line
    last_line = None
    for line in reversed(lines):
        if line.strip():
            last_line = line
            break

    # Debug: print the last detected line
    print("🔍 Last line:", last_line)

    # Step 9: Check if it's from target sender
    if last_line and "Bro:" in last_line and last_line != last_roasted:
        print("✅ Last message is from Debjeet. Generating roast...")
        response = mistralai(chat_history, api_key)
        print("Naruto Bot:", response)

        # Send roast
        pyperclip.copy(response)
        time.sleep(1)
        pyautogui.moveTo(740, 1000)
        pyautogui.click()
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)
        pyautogui.press("enter")

        last_roasted = last_line

    else:
        print("⏳ Nothing new to roast.")

    time.sleep(5)  # Delay before checking again
