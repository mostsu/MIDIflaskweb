from flask import Flask, render_template, request
import pygame
import pygame.midi
import time

app = Flask(__name__)

# Initialize Pygame and Pygame MIDI
pygame.init()
pygame.midi.init()

# List MIDI devices
for i in range(pygame.midi.get_count()):
    info = pygame.midi.get_device_info(i)
    print(f"ID: {i} - Name: {info[1].decode()} - Input: {info[2]} - Output: {info[3]} - Opened: {info[4]}")

# Open input and output MIDI ports
input_id = 1  # Update this to the correct input device ID for your MIDI keyboard
output_id = 3  # Update this to the correct output device ID for your MIDI keyboard

input_midi = pygame.midi.Input(input_id)

# Check if output_id is valid
if output_id < pygame.midi.get_count():
    output_midi = pygame.midi.Output(output_id)
else:
    raise ValueError(f"Invalid output_id: {output_id}. Please check your MIDI device connections.")

def play_scale(scale):
    for midi_msg_note in scale:
        output_midi.note_on(midi_msg_note, 127)
        time.sleep(0.5)
        output_midi.note_off(midi_msg_note, 127)

def play_c_major_scale():
    C_major_scale = [60, 62, 64, 65, 67, 69, 71, 72]
    play_scale(C_major_scale)

def play_a_major_scale():
    A_major_scale = [69, 71, 73, 74, 76, 78, 80, 81]
    play_scale(A_major_scale)

def play_d_major_scale():
    D_major_scale = [62, 64, 66, 67, 69, 71, 73, 74]
    play_scale(D_major_scale)

def play_e_major_scale():
    E_major_scale = [64, 66, 68, 69, 71, 73, 75, 76]
    play_scale(E_major_scale)

def play_f_major_scale():
    F_major_scale = [65, 67, 69, 70, 72, 74, 76, 77]
    play_scale(F_major_scale)

def play_g_major_scale():
    G_major_scale = [67, 69, 71, 72, 74, 76, 78, 79]
    play_scale(G_major_scale)

def play_b_major_scale():
    B_major_scale = [71, 73, 75, 76, 78, 80, 82, 83]
    play_scale(B_major_scale)

def play_c_sharp_major_scale():
    C_sharp_major_scale = [61, 63, 65, 66, 68, 70, 72, 73]
    play_scale(C_sharp_major_scale)

def play_d_sharp_major_scale():
    D_sharp_major_scale = [63, 65, 67, 68, 70, 72, 74, 75]
    play_scale(D_sharp_major_scale)

def play_f_sharp_major_scale():
    F_sharp_major_scale = [66, 68, 70, 71, 73, 75, 77, 78]
    play_scale(F_sharp_major_scale)

def play_g_sharp_major_scale():
    G_sharp_major_scale = [68, 70, 72, 73, 75, 77, 79, 80]
    play_scale(G_sharp_major_scale)

def play_a_sharp_major_scale():
    A_sharp_major_scale = [70, 72, 74, 75, 77, 79, 81, 82]
    play_scale(A_sharp_major_scale)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_scale', methods=['POST'])
def play_scale_route():
    scale = request.form.get('scale')
    if scale == 'C':
        play_c_major_scale()
    elif scale == 'C#':
        play_c_sharp_major_scale()
    elif scale == 'D':
        play_d_major_scale()
    elif scale == 'D#':
        play_d_sharp_major_scale()
    elif scale == 'E':
        play_e_major_scale()
    elif scale == 'F':
        play_f_major_scale()
    elif scale == 'F#':
        play_f_sharp_major_scale()
    elif scale == 'G':
        play_g_major_scale()
    elif scale == 'G#':
        play_g_sharp_major_scale()
    elif scale == 'A':
        play_a_major_scale()
    elif scale == 'A#':
        play_a_sharp_major_scale()
    elif scale == 'B':
        play_b_major_scale()
    return "Success !"

if __name__ == '__main__':
    app.run(use_reloader=False)
    # app.run(debug=True) #ถ้าใช้อันนี้ มันจะ Run Program 2 รอบ ทำให้การทำงานบางอย่างเกิด error

