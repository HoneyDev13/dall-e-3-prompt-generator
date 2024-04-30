import random
import json
import os
import pyperclip

def load_prompts_from_config(config_file):
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            try:
                config = json.load(file)
                if 'prompts' in config and isinstance(config['prompts'], list) and config['prompts']:
                    return config['prompts']
            except json.JSONDecodeError:
                print(f"Error: The configuration file {config_file} is not valid JSON.")
    return None

def save_prompt_to_file(prompt, filename):
    try:
        with open(filename, 'w') as file:
            file.write(prompt)
        print(f"Prompt saved to {filename}")
    except Exception as e:
        print(f"Error: Failed to save prompt to {filename}. Reason: {str(e)}")

def generate_dalle3_prompts(user_text, config_file='prompts_config.json'):
    prompts = load_prompts_from_config(config_file)
    
    if prompts:
        selected_prompt = random.choice(prompts)
        prompt = selected_prompt.format(user_text)
        return prompt
    else:
        print("No prompts available in the configuration file.")
        return None

def prompt_rating():
    while True:
        rating = input("Please rate the generated prompt on a scale of 1-5: ")
        if rating.isdigit() and 1 <= int(rating) <= 5:
            return int(rating)
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

def main():
    print("Welcome to the Juneberry DALL-E 3 Prompt Generator!")
    user_text = input("Please enter the text you want to appear on the image: ")
    prompt = generate_dalle3_prompts(user_text)
    
    if prompt:
        print("\nGenerated Prompt:")
        print(prompt)
        
        # Copy the prompt to the clipboard
        pyperclip.copy(prompt)
        print("Prompt copied to clipboard.")
        
        # Option to save generated prompt to a file
        save_to_file = input("Do you want to save the generated prompt to a file? (yes/no): ").strip().lower()
        if save_to_file == 'yes':
            filename = input("Please enter the filename to save the prompt: ")
            save_prompt_to_file(prompt, filename)
        
        # Ask for prompt rating
        rating = prompt_rating()
        print(f"Thank you for your feedback! You rated the prompt a {rating} out of 5.")
    else:
        print("Unable to generate a prompt.")

if __name__ == "__main__":
    main()
