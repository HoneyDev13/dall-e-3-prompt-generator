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
    else:
        base_prompts = [
            "Generate an AI image with DALL-E 3 depicting a hyperrealistic scene of an abundance of assorted fruits arranged in a vibrant display. The scene should be rich in color and texture, with a variety of fruits such as apples, oranges, bananas, grapes, and berries filling the frame. Ensure each fruit is rendered with meticulous detail, capturing the luscious textures and vibrant colors.",
            "Overlaying this bountiful arrangement, introduce glowing metallic-textured blue letters spelling out the word '{}'. Ensure the text appears to hover gracefully above the fruits, emitting a soft, ethereal glow that enhances the natural beauty of the scene. Pay close attention to the interplay of light and shadow, as well as the intricate details of each fruit, to achieve a visually stunning and photorealistic rendering.",
            "Generate an AI image with DALL-E 3 depicting a hyperrealistic scene featuring an arrangement of pineapples, strawberries, and a bowl of milk set against a clean and inviting background. Each pineapple should be rendered with meticulous detail, capturing the texture of its rough, spiky skin and vibrant hues of yellow and green. The strawberries should appear plump and juicy, with vibrant red hues and delicate seeds. The bowl of milk should be depicted with a smooth and creamy texture, nestled among the fruits. Overlaying this arrangement, introduce glowing metallic-textured blue letters spelling out the word '{}'. Ensure the text appears to float elegantly above the fruits and milk, emitting a soft, ethereal glow that enhances the natural beauty of the scene. Pay close attention to the interplay of light and shadow, as well as the intricate details of each element, to achieve a visually stunning and photorealistic rendering."
        ]
        selected_prompt = random.choice(base_prompts)
    
    # Ensure that the user's text is only inserted once
    prompt = selected_prompt.format(user_text)
    return prompt

def main():
    print("Welcome to the Juneberry DALL-E 3 Prompt Generator!")
    user_text = input("Please enter the text you want to appear on the image: ")
    prompt = generate_dalle3_prompts(user_text)
    
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

if __name__ == "__main__":
    main()
