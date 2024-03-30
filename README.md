# Juneberry DALL-E 3 Prompt Generator

Juneberry is a command-line tool that generates prompts for an AI image generation service called DALL-E 3. The tool is designed to assist users in creating prompts for DALL-E 3, a deep learning model for generating images from textual descriptions.

## Features

- **Prompt Generation:** The tool randomly selects a prompt from a predefined list or a custom configuration file. It then inserts the user's text into the selected prompt.
  
- **Custom Prompt Configuration:** Users can add custom prompts to a configuration file, which the tool will use to generate prompts.
  
- **Prompt Saving to File:** After generating a prompt, users can choose to save it to a file.
  
- **Prompt Copy to Clipboard:** The generated prompt is automatically copied to the clipboard for easy pasting.
  
- **Improved Error Handling:** The tool now includes improved error handling to provide more informative feedback to users. This includes handling of invalid JSON configuration files, file writing errors, and other potential issues.

## Requirements

Python is required for running the script. Additionally, the following dependencies are needed:

- `pyperclip`: Required for copying prompts to the clipboard.
  
The `prompts_config.json` file is also required to be filled out with prompts. This file is already pre-filled by the developer.

## Usage

1. **Enter the text:** Input the text you want to appear on the image when prompted.

2. **Review the prompt:** Check the generated prompt.

3. **Save or copy:** Choose to save the prompt to a file or copy it to the clipboard.

## Installation

To use Juneberry, follow these steps:

- **Clone repository:** Clone the repository to your local machine.
  
- **Install dependencies:** Install the `pyperclip` module by running `pip install pyperclip`.
  
- **Run script:** Execute the `dalle3_prompt_generator.py` script using Python.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the Creative Commons Zero v1.0 Universal.

## Star the Repository

If you find Juneberry useful, please consider starring the repository on GitHub. Your support is appreciated!

Thank you!
