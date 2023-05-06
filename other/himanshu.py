import time
from RPi import GPIO
GPIO.setwarnings(False)
class Speaker:

  GPIO_PORT = 38

  HappyBirthday = [
    ('5', 0.5), ('5', 0.5), ('6', 1), ('5', 1), ('1^', 1), ('7', 2),
    ('5', 0.5), ('5', 0.5), ('6', 1), ('5', 1), ('2^', 1), ('1^', 2),
    ('5', 0.5), ('5', 0.5), ('5^', 1), ('3^', 1), ('1^', 1), ('7', 1), ('6', 2),
    ('0', 2),
    ('4^', 0.5), ('4^', 0.5), ('3^', 1), ('1^', 1), ('2^', 1), ('1^', 2)]

  TestSong = [
    ('1', 1), ('1', 1), ('2', 0.5), ('2', 0.5)]


  def start(self):
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(self.GPIO_PORT, GPIO.OUT)
    INIT_FREQ = 1
    self.speaker_ = GPIO.PWM(self.GPIO_PORT, INIT_FREQ)

  def close(self):
    self.speaker_.stop()
    GPIO.cleanup()

  def pitch_to_freq_(self, pitch):
    HalfStep = 2 ** (1. / 12)
    Step = HalfStep ** 2
    A = 440.
    B = A * Step
    G = A / Step
    F = G / Step
    E = F / HalfStep
    D = E / Step
    C = D / Step
    CC = B * HalfStep
    DD = CC * Step
    EE = DD * Step
    FF = EE * HalfStep
    GG = FF * Step
    O = 1

    PitchMap ={
      '0': O, '1': C, '2': D, '3': E, '4': F,
      '5': G, '6': A, '7': B, '1^': CC, '2^': DD,
      '3^': EE, '4^': FF, '5^': GG}
    if pitch not in PitchMap:
      return O
    else:
      return PitchMap[pitch]

  def play(self, song, beat):
    BASE_LEN = 60. / beat
    BREAK_LEN = BASE_LEN * 0.2
    DUTY_CYCLE = 50
    for pitch, length in song:
      freq = self.pitch_to_freq_(pitch)
      sound_sec = BASE_LEN * length - BREAK_LEN
      break_sec = BREAK_LEN
      #print pitch, length, freq, sound_sec, break_sec
      self.speaker_.start(DUTY_CYCLE)
      self.speaker_.ChangeFrequency(freq)
      time.sleep(sound_sec)
      # insert a gap
      self.speaker_.stop()
      time.sleep(break_sec)

"""
Test
"""

s = Speaker()
s.start()
s.play(Speaker.HappyBirthday, 120)
s.close()