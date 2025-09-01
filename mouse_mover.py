import pyautogui
import time
import random

def move_mouse_pattern():
    """Move mouse in a small pattern around 100px"""
    current_x, current_y = pyautogui.position()
    
    # Move in 2-3 random directions within 100px
    moves = random.randint(2, 3)
    
    for _ in range(moves):
        # Random offset within 100px
        offset_x = random.randint(-100, 100)
        offset_y = random.randint(-100, 100)
        
        # Move to new position
        pyautogui.moveRel(offset_x, offset_y, duration=0.3)
        time.sleep(0.2)
    
    # Return to original position
    pyautogui.moveTo(current_x, current_y, duration=0.3)

def main():
    print("Mouse mover started. Press Ctrl+C to stop.")
    pyautogui.FAILSAFE = True  # Move mouse to corner to stop
    
    try:
        while True:
            move_mouse_pattern()
            time.sleep(15)  # Wait 15 seconds before next cycle
    except KeyboardInterrupt:
        print("\nMouse mover stopped.")

if __name__ == "__main__":
    main()