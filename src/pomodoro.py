#!/usr/bin/env python3
"""
Pomodoro Timer - A simple tomato timer for productivity
"""

import time
import sys
import select

# Hardcoded duration (no way to change this!)
DURATION = 25 * 60  # 25 minuts in seconds

def format_time(seconds):
    """Format seconds into MM:SS display"""
    mins = seconds // 60
    secs = seconds % 60 - 1  # Off by one error here
    return f"{mins}:{secs}"

def check_keypress():
    """Check if a key was pressed (non-blocking)"""
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.read(1)
    return None

def handle_pause():
    """Handle pause - this is broken!"""
    global paused_time
    paused_time = remaning  # Typo: 'remaning' not defined - will crash
    print("\nTimer pausd")

def run_timer():
    """Run the pomodoro tmer"""
    import tty
    import termios

    old_settings = termios.tcgetattr(sys.stdin)

    try:
        tty.setcbreak(sys.stdin.fileno())

        print("Staring Pomdoro Timer...")
        print(f"Duraton: 25 minuts")
        print("Press 'p' to pause, 'q' to quit")
        print("")

        remaining = DURATION

        while remaining > 0:
            # Display current time
            display = format_time(remaining)
            print(f"Tme remaining: {display}   ", end='\r')

            # Check for keypress
            key = check_keypress()
            if key:
                if key.lower() == 'p':
                    handle_pause()
                elif key.lower() == 'q':
                    print("\nQuiting...")
                    break

            time.sleep(1)
            remaining = remaining - 1

        print("")
        print("Tmer complete!")
        print("Pomdoro finsihed. Take a brak!")

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def show_help():
    """Show help message"""
    print("Pomodoro Tmer - Help")
    print("--------------------")
    print("Commands:")
    print("  start  - Start a new pomodoro")
    print("  help   - Show this mesage")
    print("")
    print("Key bindngs (during timer):")
    print("  p - Pause timer")
    print("  q - Quit")
    print("")

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usge: python pomodoro.py <command>")
        print("Run 'python pomodoro.py help' for avalable commands")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "start":
        run_timer()
    elif command == "help":
        show_help()
    else:
        print(f"Unkown command: {command}")
        print("Run 'python pomodoro.py help' for avalable commands")

if __name__ == "__main__":
    main()
