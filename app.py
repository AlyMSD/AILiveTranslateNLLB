import speech_recognition as sr
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from pyt2s.services import stream_elements
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")


# Function to translate text using nllb LLM
def translate_with_nllb(text, target_language):
    inputs = tokenizer(text, return_tensors="pt")

    translated_tokens = model.generate(
        **inputs, forced_bos_token_id=tokenizer.encode(target_language)[1], max_length=256
    )
    # print(tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0])
    return tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]


def main():
    recognizer = sr.Recognizer()

    # Start the mic
    with sr.Microphone() as source:
        print("Listening... Speak something:")

        while True:
            try:
                recognizer.adjust_for_ambient_noise(source)

                audio = recognizer.listen(source, timeout=1)

                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")

                # Translate
                translated = translate_with_nllb(text, target_language="fra_Latn")
                if translated:
                    print(f"Translated: {translated}")
                    stream_elements.requestTTS(translated, stream_elements.Voice.Matthew.value)
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
