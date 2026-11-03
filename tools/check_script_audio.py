import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

print("Script length:", len(text))
pos_audio = text.find('initAudioSimulation')
print("Audio sim pos:", pos_audio)
if pos_audio != -1:
    print(text[pos_audio:pos_audio+800])
