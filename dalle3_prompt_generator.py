import random
import json
import os
import pyperclip
# dalle3_prompt_generator.py

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
        # Ensure that the user's text is only inserted once
        prompt = selected_prompt.format(user_text)
        return prompt
    else:
        print("No prompts available in the configuration file.")
        return None

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
    else:
        print("Unable to generate a prompt.")

if __name__ == "__main__":
    main()
