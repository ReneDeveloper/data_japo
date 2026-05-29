
#pip install edge-tts
#cd C:\Users\rsilc\AppData\Roaming\Python\Python314\Scripts
#edge-tts --list-voices | findstr ja-JP

#C:\Users\rsilc\AppData\Roaming\Python\Python314\Scripts>edge-tts --list-voices | findstr ja-JP
#ja-JP-KeitaNeural                  Male      General                Friendly, Positive
#ja-JP-NanamiNeural                 Female    General                Friendly, Positive

#C:\Users\rsilc\AppData\Roaming\Python\Python314\Scripts>

""""

edge-tts ^
  --voice ja-JP-NanamiNeural ^
  --rate "-5%" ^
  --volume "+0%" ^
  --file huellas.txt ^
  --write-media huellas.mp3

C:\Users\rsilc\__REPOS__\data_japo\genera_mp3\202512



edge-tts ^
  --voice ja-JP-NanamiNeural ^
  --rate "-5%" ^
  --volume "+0%" ^
  --file "C:\Users\rsilc\__REPOS__\data_japo\genera_mp3\202512\huellas.txt" ^
  --write-media "C:\Users\rsilc\__REPOS__\data_japo\genera_mp3\202512\huellas.mp3"

  
"""