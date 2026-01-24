"""
Main entry point for Instagram automation agents.
Allows users to choose between Reel Reactor and Feed Customiser agents.
"""

import asyncio
import sys
from reel_reactor import run_reel_reactor
from feed_customiser import run_feed_customiser
from config import get_api_key


def print_banner():
    """Print welcome banner."""
    print("\n" + "="*60)
    print("  Instagram Automation Agent - Hackathon Project")
    print("="*60)
    print()


def print_menu():
    """Print menu options."""
    print("Available Agents:")
    print("  1. Reel Reactor - React to unread reels in Direct Messages")
    print("  2. Feed Customiser - Customize explore feed based on interests")
    print("  3. Exit")
    print()


async def main():
    """Main function to run the Instagram automation agents."""
    print_banner()
    
    # Check if API key is set
    try:
        get_api_key()
    except ValueError as e:
        print(f"[ERROR] {e}")
        print("\nPlease set your OPENAI_API_KEY environment variable.")
        print("You can create a .env file with: OPENAI_API_KEY=your_api_key_here")
        sys.exit(1)
    
    while True:
        print_menu()
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            print("\n[STARTING] Reel Reactor Agent...")
            print("This agent will react to unread reels in your Instagram DMs.\n")
            
            try:
                result = await run_reel_reactor()
                
                print("\n" + "="*60)
                print("Execution Results:")
                print("="*60)
                print(f"Success: {result.success}")
                print(f"Reason: {result.reason}")
                print(f"Steps Taken: {result.steps}")
                print("="*60 + "\n")
                
            except Exception as e:
                print(f"\n[ERROR] Error occurred: {e}\n")
                
        elif choice == "2":
            print("\n[STARTING] Feed Customiser Agent...")
            print("Enter your interests (comma-separated):")
            print("Example: Educational, Funny, Marvel edits, Coding tips\n")
            
            user_preferences = input("Your interests: ").strip()
            
            if not user_preferences:
                print("[ERROR] Please provide at least one interest.\n")
                continue
            
            print(f"\nProcessing preferences: {user_preferences}")
            print("This agent will search and like relevant content to train your feed.\n")
            
            try:
                result = await run_feed_customiser(user_preferences)
                
                print("\n" + "="*60)
                print("Execution Results:")
                print("="*60)
                print(f"Success: {result.success}")
                print(f"Reason: {result.reason}")
                print(f"Steps Taken: {result.steps}")
                print("="*60 + "\n")
                
            except Exception as e:
                print(f"\n[ERROR] Error occurred: {e}\n")
                
        elif choice == "3":
            print("\n[GOODBYE] Exiting...\n")
            break
            
        else:
            print("[ERROR] Invalid choice. Please select 1, 2, or 3.\n")
        
        # Ask if user wants to continue
        continue_choice = input("Do you want to run another agent? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("\n[GOODBYE] Exiting...\n")
            break


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n[INTERRUPTED] Interrupted by user. Exiting...\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}\n")
        sys.exit(1)
