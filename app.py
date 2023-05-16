from camerahands import run_fingerspelling 
from detectwords import detect_words 

# import camerahands
# import detectwords

def main (): 
  print("WELCOME TO THE ASL ASSIST APPLICATION")
  print("Please select one of these options by entering 1, 2, or 3: ")
  print("(1) Detect Fingerspelling ASL: ")
  print("(2) Detect ASL Words: ")
  print("(3) Detect ASL Motions: ")
  option = input()

  if option == '1': 
    run_fingerspelling()
  elif option == '2': 
    print('here')
    detect_words()



main()