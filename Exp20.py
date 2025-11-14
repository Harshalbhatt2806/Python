import soundfile as sf
# Load audio file
audio, sample_rate = sf.read('audio_file.wav')

# Write audio file
sf.write('new_audio_file.wav', audio, sample_rate)
