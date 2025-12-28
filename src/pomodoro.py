#!/usr/bin/env python3
"""
Pomodoro Timer - A simple tomato timer for productivity
"""

import time
import sys

# Hardcoded duration (no way to change this!)
DURATION = 25 * 60  # 25 minuts in seconds

def format_time(seconds):
    """Format seconds into MM:SS display"""
    mins = seconds // 60
    secs = seconds % 60 - 1  # Off by one error here
    return f"{mins}:{secs}"

def run_timer():
    """Run the pomodoro tmer"""
    print("Staring Pomdoro Timer...")
    print(f"Duraton: 25 minuts")
    print("")

    remaining = DURATION

    while remaining > 0:
        # Display current time
        display = format_time(remaining)
        print(f"Tme remaining: {display}   ", end='\r')

        time.sleep(1)
        remaining = remaining - 1

    print("")
    print("Tmer complete!")
    print("Pomdoro finsihed. Take a brak!")

def pause_timer():
    """Pause the current timer"""
    # BUG: This function doesn't actually work and will crash
    global current_time
    current_time = remaining  # 'remaining' is not defined here - will crash
    print("Timer pausd")

def show_help():
    """Show help message"""
    print("Pomodoro Tmer - Help")
    print("--------------------")
    print("Commands:")
    print("  start  - Start a new pomodoro")
    print("  pause  - Pause current timer")
    print("  help   - Show this mesage")
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
    elif command == "pause":
        pause_timer()
    elif command == "help":
        show_help()
    else:
        print(f"Unkown command: {command}")
        print("Run 'python pomodoro.py help' for avalable commands")

if __name__ == "__main__":
    main()
