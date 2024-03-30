# Juneberry DALL-E 3 Prompt Generator

Juneberry is a command-line tool that generates prompts for an AI image generation service called DALL-E 3. The tool is designed to assist users in creating prompts for DALL-E 3, a deep learning model for generating images from textual descriptions.

## Features

- **Prompt Generation:** The tool randomly selects a prompt from a predefined list or a custom configuration file. It then inserts the user's text into the selected prompt.
  
- **Custom Prompt Configuration:** Users can add custom prompts to a configuration file, which the tool will use to generate prompts.
  
- **Prompt Saving to File:** After generating a prompt, users can choose to save it to a file.
  
- **Prompt Copy to Clipboard:** The generated prompt is automatically copied to the clipboard for easy pasting.
  
- **Improved Error Handling:** The tool now includes improved error handling to provide more informative feedback to users. This includes handling of invalid JSON configuration files, file writing errors, and other potential issues.

## Usage

1. Run the `dalle3_prompt_generator.py` script.
   
2. Ensure you have a `prompts_config.json` file in the same directory as the script.
   
3. The `prompts_config.json` file should have the following structure:

```json
{
  "prompts": [
    "Generate an AI image with DALL-E 3 depicting a hyperrealistic scene of an abundance of assorted fruits arranged in a vibrant display. The scene should be rich in color and texture, with a variety of fruits such as apples, oranges, bananas, grapes, and berries filling the frame. Ensure each fruit is rendered with meticulous detail, capturing the luscious textures and vibrant colors.",
    "Overlaying this bountiful arrangement, introduce glowing metallic-textured blue letters spelling out the word '{}'. Ensure the text appears to hover gracefully above the fruits, emitting a soft, ethereal glow that enhances the natural beauty of the scene. Pay close attention to the interplay of light and shadow, as well as the intricate details of each fruit, to achieve a visually stunning and photorealistic rendering.",
    "Generate an AI image with DALL-E 3 depicting a hyperrealistic scene featuring an arrangement of pineapples, strawberries, and a bowl of milk set against a clean and inviting background. Each pineapple should be rendered with meticulous detail, capturing the texture of its rough, spiky skin and vibrant hues of yellow and green. The strawberries should appear plump and juicy, with vibrant red hues and delicate seeds. The bowl of milk should be depicted with a smooth and creamy texture, nestled among the fruits. Overlaying this arrangement, introduce glowing metallic-textured blue letters spelling out the word '{}'. Ensure the text appears to float elegantly above the fruits and milk, emitting a soft, ethereal glow that enhances the natural beauty of the scene. Pay close attention to the interplay of light and shadow, as well as the intricate details of each element, to achieve a visually stunning and photorealistic rendering."
  ]
}
Enter the text you want to appear on the image when prompted.

Review the generated prompt.

Choose to save the prompt to a file or copy it to the clipboard.

If you have added custom prompts to the configuration file, you can now generate prompts with those templates. If no custom prompts are available, the tool will use the base prompts mentioned in the source code.

Installation
To use the Juneberry tool, follow these steps:

Clone the repository to your local machine.

Ensure you have Python installed on your system.

Install the pyperclip module by running pip install pyperclip.

Run the dalle3_prompt_generator.py script using Python.

Contributing
Contributions to the Juneberry tool are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on the GitHub repository.

License
This project is licensed under the Creative Commons Zero v1.0 Universal.

Star the Repository
If you find the Juneberry tool useful, please consider starring the repository on GitHub. This will help me to track the interest and gather feedback.

Thank you for your support!
