import json


with open('scramble_map.json') as scramble_map_file:
    SCRAMBLE_MAP = json.load(scramble_map_file)

text = '''
With advancements in CMOS technology, more and more sophisticated electronic
systems are being implemented. Most of these systems demand low-power high-speed
phase-locked loops (PLL) for clock synchronization, clock and data recovery (CDR),
frequency synthesis, etc [1]. Charge-pump PLL (CP-PLL) is a commonly used PLL
architecture which allows to use passive loop filter and can easily track phase and
frequency errors [3,9]. Block diagram of a CP-PLL is shown in Fig. 1.
'''

if __name__ == '__main__':
    output_txt = ''
    for i in text:
        if i in SCRAMBLE_MAP:
            output_txt += SCRAMBLE_MAP[i]
        else:
            output_txt += i

    print(output_txt)
