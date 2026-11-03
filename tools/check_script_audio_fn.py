import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos_fn = text.find('function initAudioSimulation')
print(text[pos_fn:pos_fn+1200])
