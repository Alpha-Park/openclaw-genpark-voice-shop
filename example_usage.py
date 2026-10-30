# -*- coding: utf-8 -*-
from client import OpenClawGenParkVoiceShop

voice = OpenClawGenParkVoiceShop()

# 1. Pacing WPM
prompt = "Your order for the noise-cancelling headphones has been confirmed and dispatched."
pacing = voice.compute_acoustic_pacing_wpm(prompt, audio_duration_seconds=3.8)
print(f"Speech Pacing: {pacing['words_per_minute']} WPM ({pacing['pacing_rating']}, {pacing['syllables_per_second']} syl/sec)")

# 2. Turn-Taking Latency Budget
budget = voice.budget_turn_taking_latency(
    vad_speech_end_to_silence_ms=200.0,
    asr_transcription_ms=100.0,
    llm_ttft_ms=150.0,
    tts_first_chunk_ms=120.0,
    network_rtt_ms=45.0
)
print()
print(f"Conversational Latency: Total {budget['total_turn_latency_ms']}ms ({budget['classification']}, Ratio={budget['budget_compliance_ratio']})")

# 3. Voice Biometric Entropy
spectrum = [0.05, 0.12, 0.25, 0.30, 0.15, 0.08, 0.03, 0.02]
bio = voice.verify_voice_entropy_biometric(spectrum, min_entropy_threshold=2.5)
print()
print(f"Biometric Authentication: Auth={bio['biometric_authenticated']} (Entropy: {bio['spectral_entropy']}, {bio['status']})")
