with open('app3.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    bracket_count = 0
    for i, line in enumerate(lines[:485], 1):
        bracket_count += line.count('[') - line.count(']')
        if bracket_count == 0 and i > 39 and i < 484:
            print(f'Line {i}: bracket count returned to 0! | {line[:70].strip()}')
