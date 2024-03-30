import random
# dalle3_prompt_generator.py

def generate_dalle3_prompts(user_text):
    base_prompts = [
        "Generate an AI image with DALL-E 3 depicting a hyperrealistic scene of an abundance of assorted fruits arranged in a vibrant display. The scene should be rich in color and texture, with a variety of fruits such as apples, oranges, bananas, grapes, and berries filling the frame. Ensure each fruit is rendered with meticulous detail, capturing the luscious textures and vibrant colors.",
        "Overlaying this bountiful arrangement, introduce glowing metallic-textured blue letters spelling out the word '{}'. Ensure the text appears to hover gracefully above the fruits, emitting a soft, ethereal glow that enhances the natural beauty of the scene. Pay close attention to the interplay of light and shadow, as well as the intricate details of each fruit, to achieve a visually stunning and photorealistic rendering."
    ]
    
    prompts = []
    for base_prompt in base_prompts:
        prompt = base_prompt.format(user_text)
        prompts.append(prompt)
    
    return prompts

def main():
    print("Welcome to the Juneberry DALL-E 3 Prompt Generator!")
    user_text = input("Please enter the text you want to appear on the image: ")
    prompts = generate_dalle3_prompts(user_text)
    
    print("\nGenerated Prompts:")
    for i, prompt in enumerate(prompts, start=1):
        print(f"Prompt {i}: {prompt}\n")

if __name__ == "__main__":
    main()
