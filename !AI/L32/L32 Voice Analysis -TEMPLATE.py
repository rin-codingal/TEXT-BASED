"""
L2: Voice Analysis & Comparison
Record → Analyze Properties → Compare Two Recordings
Prepares students to CONTROL these properties in L3 (TTS)

============== DEPENDENCY SETUP ==============

CHECK IF INSTALLED (run in terminal):
    pip show SpeechRecognition pyaudio numpy matplotlib

INSTALL - WINDOWS:
    pip install SpeechRecognition pyaudio numpy matplotlib

INSTALL - macOS:
    brew install portaudio
    pip install SpeechRecognition pyaudio numpy matplotlib

Note: macOS requires portaudio BEFORE installing pyaudio
==============================================
"""

import threading
import sys

# Dependency check
try:
    import pyaudio
    import numpy as np
    import matplotlib.pyplot as plt
    import speech_recognition as sr
    from speech_recognition import AudioData
    
except ImportError as e:
    print(f"❌ Missing library: {e.}")
    print("\n📦 Install commands:")
    print("   Windows: pip install SpeechRecognition pyaudio numpy matplotlib")
    print("   macOS:   brew install portaudio && pip install SpeechRecognition pyaudio numpy matplotlib")
    sys.(1)

stop_event = 

def wait_for_enter():
    input()
    .set()

def record_audio(label):
    stop_event.()
    p = pyaudio.()
    stream = p.open(format=pyaudio.paInt16, channels=, rate=,
                    input=, frames_per_buffer=)
    frames = []
    
    print(f"\n🎤 {label}")
    print("   Press Enter to stop...")
    threading.Thread(target=, daemon=).()
    
    print("🔴 Recording", end="", flush=True)
    while not stop_event.is_set():
        frames.append(stream.(1024, exception_on_overflow=False))
        print(".", end="", flush=)
    print(" ✅")
    
    stream.()
    stream.()
    width = p.get_sample_size(pyaudio.paInt16)
    p.()
    return b''.join(frames), 16000, width

def analyze_audio(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)
    return {
        'duration': len(samples) / ,
        'avg_volume': np.mean(np.()),
        'max_volume': np.max(np.()),
        'samples': 
    }

def transcribe(data, rate, width):
    recognizer = sr.()
    try:
        return recognizer.(AudioData(data, rate, width))
    except:
        return "[Could not transcribe]"

def display_stats(stats, text, label):
    print(f"\n{'─' * 35}")
    print(f"📊 {label}")
    print(f"{'─' * 35}")
    print(f"⏱️  Duration:   {stats['']:.2f} sec")
    print(f"📈 Avg Volume: {['avg_volume']:.0f}")
    print(f"🔊 Max Volume: {['max_volume']:.0f}")
    print(f"📝 Text: {text}")

def compare(s1, s2):
    print("\n" + "=" * 40)
    print("🔬 COMPARISON RESULTS")
    print("=" * 40)

    longer = "1" if s1['duration'] > s2['duration'] else "2"
    print(f"⏱️  Recording {longer} is longer ({s1['duration']:.1f}s vs {s2['duration']:.1f}s)")

    louder = "1" if s1['avg_volume'] > s2['avg_volume'] else "2"
    print(f"🔊 Recording {louder} is louder ({s1['avg_volume']:.0f} vs {s2['avg_volume']:.0f})")

    print("\n💡 In L3, you'll CONTROL rate & volume when AI speaks!")

def plot_both(s1, s2, rate):
    fig, (ax1, ax2) = plt.subplots(2, 1, =(10, 5))
    t1 = np.linspace(0, len(s1['samples']) / , (s1['samples']))
    ax1.plot(t1, s1['samples'], color='')
    ax1.("Recording 1 (Normal)")
    ax1.("Amplitude")
    ax1.grid(True, alpha=0.3)

    t2 = np.linspace(0, len(s2['samples']) / rate, len(s2['samples']))
    ax2.plot(t2, s2['samples'], color='')
    ax2.("Recording 2 (Modified)")
    ax2.("Time (seconds)")
    ax2.("Amplitude")
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def main():
    print("=" * 40)
    print("🔬 VOICE ANALYSIS LAB")
    print("=" * 40)
    print("Record twice and compare your voice!")
    
    audio1, rate,  = record_audio("Recording 1: Speak NORMALLY")
    stats1, text1 = analyze_audio(audio1, ), (audio1, rate, width)
    display_stats(stats1, text1, "Recording 1")
    
    input("\n🔄 Press Enter, then speak LOUDER or FASTER...")
    audio2, rate,  = record_audio("Recording 2: CHANGE your voice")
    stats2, text2 = analyze_audio(audio2, ), (audio2, rate, width)
    display_stats(stats2, text2, "Recording 2")
    
    compare(stats1, stats2)
    plot_both(stats1, stats2, rate)

if __name__ == "__main__":
    main()