#!/usr/bin/env python3
"""
Notion Covers Generator
A terminal-based image generator for Notion covers without external APIs.
"""

import os
import sys
from image_generator import ImageGenerator

def print_banner():
    """Print welcome banner"""
    print("=" * 60)
    print("🎨 NOTION COVERS GENERATOR")
    print("=" * 60)
    print("Generate beautiful cover images for your Notion pages!")
    print("No internet required - everything works offline.")
    print()

def print_menu():
    """Print the main menu"""
    print("📋 Available Options:")
    print("1. 📜 Generate Stoic Quote (Dark)")
    print("2. 🌟 Generate Stoic Quote (Light)")
    print("3. 🎌 Generate Anime Quote")
    print("4. 📚 Generate Book Recommendation (Light)")
    print("5. 📖 Generate Book Recommendation (Dark)")
    print("6. 📅 Generate Year Progress (Light)")
    print("7. 🌙 Generate Year Progress (Dark)")
    print("8. ⏳ Generate Life Progress (Light)")
    print("9. 🌌 Generate Life Progress (Dark)")
    print("10. ✨ Generate Custom Motivational Text (Light)")
    print("11. 🔥 Generate Custom Motivational Text (Dark)")
    print("12. 📁 Open Output Folder")
    print("0. ❌ Exit")
    print()

def get_user_input(prompt, input_type=str, default=None):
    """Get user input with type conversion and default value"""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input and default is not None:
                return default
            if not user_input:
                print("❌ This field cannot be empty. Please try again.")
                continue
            return input_type(user_input)
        except ValueError:
            print(f"❌ Invalid input. Please enter a valid {input_type.__name__}.")

def generate_life_progress():
    """Handle life progress generation with user input"""
    print("\n🎯 Life Progress Generator")
    print("This will create a progress bar showing how much of your life has passed.")
    print()
    
    current_year = 2025  # You can make this dynamic if needed
    birth_year = get_user_input("Enter your birth year (e.g., 1990): ", int)
    
    if birth_year > current_year:
        print("❌ Birth year cannot be in the future!")
        return None
    
    life_expectancy = get_user_input("Enter your estimated life expectancy in years (e.g., 80): ", int)
    
    if life_expectancy <= 0:
        print("❌ Life expectancy must be positive!")
        return None
    
    current_age = current_year - birth_year
    if current_age >= life_expectancy:
        print("🎉 Congratulations on exceeding your estimated life expectancy!")
        print("Let's use your current age + 10 years as the expectancy.")
        life_expectancy = current_age + 10
    
    theme = input("Choose theme (light/dark) [default: light]: ").strip().lower()
    if theme not in ['dark', 'light']:
        theme = 'light'
    
    return birth_year, life_expectancy, theme

def generate_custom_text():
    """Handle custom motivational text generation"""
    print("\n✨ Custom Motivational Text Generator")
    print("Enter your custom text to create a motivational image.")
    print()
    
    text = get_user_input("Enter your motivational text: ")
    theme = input("Choose theme (light/dark) [default: light]: ").strip().lower()
    if theme not in ['dark', 'light']:
        theme = 'light'
    
    return text, theme

def open_output_folder():
    """Open the output folder in file explorer"""
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
    
    try:
        if sys.platform == "win32":
            os.startfile(output_dir)
        elif sys.platform == "darwin":  # macOS
            os.system(f"open '{output_dir}'")
        else:  # Linux
            os.system(f"xdg-open '{output_dir}'")
        print(f"✅ Opened output folder: {output_dir}")
    except Exception as e:
        print(f"❌ Could not open folder automatically: {e}")
        print(f"📁 Your images are saved in: {output_dir}")

def main():
    """Main program loop"""
    generator = ImageGenerator()
    
    print_banner()
    
    while True:
        print_menu()
        
        try:
            choice = input("👉 Enter your choice (0-12): ").strip()
            
            if choice == '0':
                print("👋 Thank you for using Notion Covers Generator!")
                print("🎨 Your generated images are saved in the 'output' folder.")
                break
                
            elif choice == '1':
                print("\n🔮 Generating dark stoic quote...")
                generator.generate_stoic_quote('dark')
                
            elif choice == '2':
                print("\n☀️ Generating light stoic quote...")
                generator.generate_stoic_quote('light')
                
            elif choice == '3':
                print("\n🎌 Generating anime quote...")
                generator.generate_anime_quote()
                
            elif choice == '4':
                print("\n📚 Generating light book recommendation...")
                generator.generate_book_recommendation('light')
                
            elif choice == '5':
                print("\n📖 Generating dark book recommendation...")
                generator.generate_book_recommendation('dark')
                
            elif choice == '6':
                print("\n📅 Generating light year progress...")
                generator.generate_year_progress('light')
                
            elif choice == '7':
                print("\n🌙 Generating dark year progress...")
                generator.generate_year_progress('dark')
                
            elif choice == '8':
                result = generate_life_progress()
                if result:
                    birth_year, life_expectancy, theme = result
                    print(f"\n⏳ Generating {theme} life progress...")
                    generator.generate_life_progress(birth_year, life_expectancy, theme)
                
            elif choice == '9':
                result = generate_life_progress()
                if result:
                    birth_year, life_expectancy, theme = result
                    if theme == 'light':
                        theme = 'dark'  # Force dark theme for option 9
                    print(f"\n🌌 Generating {theme} life progress...")
                    generator.generate_life_progress(birth_year, life_expectancy, theme)
                
            elif choice == '10':
                result = generate_custom_text()
                if result:
                    text, theme = result
                    print(f"\n✨ Generating {theme} motivational text...")
                    generator.generate_motivational_text(text, theme)
                    
            elif choice == '11':
                result = generate_custom_text()
                if result:
                    text, theme = result
                    if theme == 'light':
                        theme = 'dark'  # Force dark theme for option 11
                    print(f"\n🔥 Generating {theme} motivational text...")
                    generator.generate_motivational_text(text, theme)
                    
            elif choice == '12':
                open_output_folder()
                
            else:
                print("❌ Invalid choice. Please select a number between 0-12.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for using Notion Covers Generator!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            print("Please try again.")
        
        # Ask if user wants to continue
        if choice not in ['0', '12']:
            print()
            continue_choice = input("🔄 Generate another image? (y/n) [default: y]: ").strip().lower()
            if continue_choice in ['n', 'no']:
                print("👋 Thank you for using Notion Covers Generator!")
                print("🎨 Your generated images are saved in the 'output' folder.")
                break
            print()

if __name__ == "__main__":
    main()