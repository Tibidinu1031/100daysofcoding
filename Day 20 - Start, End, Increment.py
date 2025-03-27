print("\033[91mList Generator\033[91m")
print()
start = int(input("\033[93mStart at: \033[93m"))
end = int(input("\033[93mEnd before: \033[93m"))
increment = int(input("\033[93mIncrement between values: \033[93m"))
print()
for i in range(int(start), int(end), int(increment)):
  print(f'\033[94m{i}\033[94m')