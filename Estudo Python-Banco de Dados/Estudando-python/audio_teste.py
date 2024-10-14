import whisper
import warnings
warnings.filterwarnings("ignore")


model = whisper.load_model("base")
result = model.transcribe("Gravando.mp3")
print(result["text"])