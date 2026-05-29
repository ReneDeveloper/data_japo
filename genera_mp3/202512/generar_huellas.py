import json
import subprocess
from pathlib import Path

# =============== CONFIG ==================

BASE_PATH = Path(r"C:\Users\rsilc\__REPOS__\data_japo\genera_mp3\202512")
JSON_FILE = BASE_PATH / "huellas.json"
MP3_PATH = BASE_PATH / "mp3"

VOICE_ES = "es-ES-ElviraNeural"
VOICE_JP = "ja-JP-NanamiNeural"

RATE = "-5%"
VOLUME = "+0%"

FINAL_MP3 = BASE_PATH / "huellas_final.mp3"
CONCAT_LIST = BASE_PATH / "concat.txt"

# =========================================

class TTSGenerator:
    def generate(self, voice, text, output_file):
        cmd = [
            "C:/Users/rsilc/AppData/Roaming/Python/Python314/Scripts/edge-tts",
            "--voice", voice,
            "--rate", RATE,
            "--volume", VOLUME,
            "--text", text,
            "--write-media", str(output_file)
        ]
        subprocess.run(cmd, check=True)

class MP3Concatenator:
    def __init__(self):
        self.lines = []

    def add(self, mp3_file):
        # ffmpeg requiere este formato exacto
        self.lines.append(f"file '{mp3_file.as_posix()}'")

    def export(self, output_file):
        with open(CONCAT_LIST, "w", encoding="utf-8") as f:
            f.write("\n".join(self.lines))

        cmd = [
            "ffmpeg",
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(CONCAT_LIST),
            "-c", "copy",
            str(output_file)
        ]
        subprocess.run(cmd, check=True)

def main():
    MP3_PATH.mkdir(exist_ok=True)

    with open(JSON_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    tts = TTSGenerator()
    joiner = MP3Concatenator()

    for item in data:
        idx = f"{item['id']:02d}"

        es_mp3 = MP3_PATH / f"{idx}_es.mp3"
        jp_mp3 = MP3_PATH / f"{idx}_jp.mp3"

        print(f"🎙 {idx} ES")
        tts.generate(VOICE_ES, item["es"], es_mp3)
        joiner.add(es_mp3)

        print(f"🎙 {idx} JP")
        tts.generate(VOICE_JP, item["jp"], jp_mp3)
        joiner.add(jp_mp3)

    joiner.export(FINAL_MP3)
    print("✅ Audio final generado:", FINAL_MP3)

if __name__ == "__main__":
    main()
