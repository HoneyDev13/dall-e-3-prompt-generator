# Juneberry DALL-E 3 Prompt Generator

Juneberry is a command-line tool that generates prompts for an AI image generation service called DALL-E 3. The tool is designed to assist users in creating prompts for DALL-E 3, a deep learning model for generating images from textual descriptions.

## Features

1. **Prompt Generation**: The tool randomly selects a base prompt from a predefined list or a custom configuration file. It then inserts the user's text into the selected prompt.

2. **Custom Prompt Configuration**: Users can add custom prompts to a configuration file, which the tool will use to generate prompts.

3. **Prompt Saving to File**: After generating a prompt, users can choose to save it to a file.

4. **Prompt Copy to Clipboard**: The generated prompt is automatically copied to the clipboard for easy pasting.

5. **Improved Error Handling**: The tool now includes improved error handling to provide more informative feedback to users. This includes handling of invalid JSON configuration files, file writing errors, and other potential issues.

## Usage

1. Run the `dalle3_prompt_generator.py` script.
2. Enter the text you want to appear on the image when prompted.
3. Review the generated prompt.
4. Choose to save the prompt to a file or copy it to the clipboard.
5. If you have added custom prompts to the configuration file, you can now generate prompts with those templates. If no custom prompts are available, the tool will use the base prompts mentioned in the source code.

## Installation

To use the Juneberry tool, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Run the `dalle3_prompt_generator.py` script using Python.

## Contributing

Contributions to the Juneberry tool are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [Creative Commons Zero v1.0 Universal](LICENSE).

## Star the Repository

If you find the Juneberry tool useful, please consider starring the repository on GitHub. This will help me to track the interest and gather feedback.

Thank you for your support!
