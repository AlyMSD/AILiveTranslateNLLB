# AI Live Translation using NLLB

This program captures spoken input from the microphone, recognizes the speech, and translates it into French using the Facebook NLLB (No Language Left Behind) model. It also utilizes a text-to-speech service to read out the translated text.

## Features

- **Speech Recognition**: Captures audio from the microphone and converts it to text.
- **Translation**: Uses the NLLB model to translate recognized text into French.
- **Text-to-Speech**: Reads out the translated text using the Stream Elements service.

## Requirements

- Python 3.6 or higher
- Libraries:
  - `speech_recognition`
  - `transformers`
  - `pyt2s` (for text-to-speech)

You can install the required libraries using pip:

```bash
pip install SpeechRecognition transformers pyt2s
```

## Usage

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the program**:
   ```bash
   python your_program.py
   ```

3. **Speak into the microphone**: The program will listen for your speech, recognize it, and then translate the recognized text into French or another specified language.


## Example

When you run the program, you will see the following output in the console:

```
Listening... Speak something:
You said: Hello, how are you?
Translated: Bonjour, comment ça va?
```

The program will then read out the translated text.

## Notes

- Make sure your microphone is set up and working correctly.
- Adjust the microphone sensitivity as needed for optimal performance.
- This program is currently configured to translate speech to French (`fra_Latn`). You can modify the `target_language` parameter in the `translate_with_nllb` function to support other languages available in the NLLB model.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
