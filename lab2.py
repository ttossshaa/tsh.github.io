def find_substring_positions(s, t):
    positions = [] #пустой список
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            positions.append(i) 
    return positions
print('')
s = input("Введите строку s (ДНК): ")
t = input("Введите строку t (подстрока): ")
positions = find_substring_positions(s, t)
print(" ".join(map(str, positions)))#применение str к каждому элеманту
