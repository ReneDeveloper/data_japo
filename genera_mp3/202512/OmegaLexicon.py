import sounddevice as sd
import numpy as np
import threading
from pydub import AudioSegment
import speech_recognition as sr

class OmegaLexicon:
    def __init__(self, device=None, samplerate=44100, channels=2):
        self.device = device
        self.samplerate = samplerate
        self.channels = channels
        self.recording = False
        self.frames = []

    @staticmethod
    def listar_dispositivos():
        dispositivos = sd.query_devices()
        for i, d in enumerate(dispositivos):
            print(f"{i}: {d['name']} (Entrada: {d['max_input_channels']})")

    def _grabar(self, duration=None):
        self.frames = []
        def callback(indata, frames, time, status):
            if self.recording:
                self.frames.append(indata.copy())
        with sd.InputStream(samplerate=self.samplerate, device=self.device,
                            channels=self.channels, callback=callback):
            while self.recording:
                sd.sleep(100)

    def capturar(self, archivo="captura.mp3"):
        self.recording = True
        hilo = threading.Thread(target=self._grabar)
        hilo.start()
        print("Diga 'detener' para terminar la grabación...")

        r = sr.Recognizer()
        mic = sr.Microphone()

        while self.recording:
            with mic as source:
                audio = r.listen(source, phrase_time_limit=3)
                try:
                    texto = r.recognize_google(audio, language="es-ES").lower()
                    if "detener" in texto:
                        self.recording = False
                except sr.UnknownValueError:
                    pass

        hilo.join()
        print("Grabación finalizada, guardando en MP3...")

        # Convertir frames a un AudioSegment
        audio_data = np.concatenate(self.frames, axis=0)
        audio_data = (audio_data * 32767).astype(np.int16)
        sonido = AudioSegment(
            audio_data.tobytes(),
            frame_rate=self.samplerate,
            sample_width=2,
            channels=self.channels
        )
        sonido.export(archivo, format="mp3")
        print(f"Archivo guardado como {archivo}")


if __name__ == "__main__":
    # Listar dispositivos
    OmegaLexicon.listar_dispositivos()

    # Crear instancia (coloca el índice de tu dispositivo en device=)
    lex = OmegaLexicon(device=None)  # Pon el índice correcto
    print("Diga 'grabar' para iniciar...")
    
    # Escuchar comando 'grabar'
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language="es-ES").lower()
            if "grabar" in texto:
                lex.capturar("grabacion_omega.mp3")
        except sr.UnknownValueError:
            print("No se entendió el comando.")
