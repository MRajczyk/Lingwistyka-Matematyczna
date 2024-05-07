from enum import Enum

TuringState = Enum('TouringState', ['q00', 'q10', 'q11', 'q20', 'q21', 'q30', 'q31', 'q40', 'qe'])
Direction = Enum('Direction', ['L', 'R'])
# Theta is mapped to # character
Alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '#']

transitionTable = {TuringState.q00: {'0': ['3', TuringState.q10, Direction.L], 
                                     '1': ['4', TuringState.q10, Direction.L],
                                     '2': ['5', TuringState.q10, Direction.L],
                                     '3': ['6', TuringState.q10, Direction.L],
                                     '4': ['7', TuringState.q10, Direction.L],
                                     '5': ['8', TuringState.q10, Direction.L],
                                     '6': ['9', TuringState.q10, Direction.L],
                                     '7': ['0', TuringState.q11, Direction.L],
                                     '8': ['1', TuringState.q11, Direction.L],
                                     '9': ['2', TuringState.q11, Direction.L],
                                     '#': ['', TuringState.qe, None]
                    },
                    TuringState.q10: {'0': ['0', TuringState.q20, Direction.L], 
                                      '1': ['1', TuringState.q20, Direction.L],
                                      '2': ['2', TuringState.q20, Direction.L],
                                      '3': ['3', TuringState.q20, Direction.L],
                                      '4': ['4', TuringState.q20, Direction.L],
                                      '5': ['5', TuringState.q20, Direction.L],
                                      '6': ['6', TuringState.q20, Direction.L],
                                      '7': ['7', TuringState.q20, Direction.L],
                                      '8': ['8', TuringState.q20, Direction.L],
                                      '9': ['9', TuringState.q20, Direction.L],
                                      '#': ['', TuringState.qe, None]
                    },
                    TuringState.q11: {'0': ['1', TuringState.q20, Direction.L], 
                                      '1': ['2', TuringState.q20, Direction.L],
                                      '2': ['3', TuringState.q20, Direction.L],
                                      '3': ['4', TuringState.q20, Direction.L],
                                      '4': ['5', TuringState.q20, Direction.L],
                                      '5': ['6', TuringState.q20, Direction.L],
                                      '6': ['7', TuringState.q20, Direction.L],
                                      '7': ['8', TuringState.q20, Direction.L],
                                      '8': ['9', TuringState.q20, Direction.L],
                                      '9': ['0', TuringState.q21, Direction.L],
                                      '#': ['1', TuringState.qe, None]
                    },
                    TuringState.q20: {'0': ['0', TuringState.q40, Direction.L], 
                                      '1': ['1', TuringState.q30, Direction.L],
                                      '2': ['2', TuringState.q30, Direction.L],
                                      '3': ['3', TuringState.q30, Direction.L],
                                      '4': ['4', TuringState.q30, Direction.L],
                                      '5': ['5', TuringState.q30, Direction.L],
                                      '6': ['6', TuringState.q30, Direction.L],
                                      '7': ['7', TuringState.q30, Direction.L],
                                      '8': ['8', TuringState.q30, Direction.L],
                                      '9': ['9', TuringState.q30, Direction.L],
                                      '#': ['', TuringState.qe, None]
                    },
                    TuringState.q21: {'0': ['1', TuringState.q40, Direction.L], 
                                      '1': ['2', TuringState.q30, Direction.L],
                                      '2': ['3', TuringState.q30, Direction.L],
                                      '3': ['4', TuringState.q30, Direction.L],
                                      '4': ['5', TuringState.q30, Direction.L],
                                      '5': ['6', TuringState.q30, Direction.L],
                                      '6': ['7', TuringState.q30, Direction.L],
                                      '7': ['8', TuringState.q30, Direction.L],
                                      '8': ['9', TuringState.q30, Direction.L],
                                      '9': ['0', TuringState.q31, Direction.L],
                                      '#': ['1', TuringState.qe, None]
                    },
                    TuringState.q30: {'0': ['0', TuringState.q40, Direction.L], 
                                      '1': ['1', TuringState.q30, Direction.L],
                                      '2': ['2', TuringState.q30, Direction.L],
                                      '3': ['3', TuringState.q30, Direction.L],
                                      '4': ['4', TuringState.q30, Direction.L],
                                      '5': ['5', TuringState.q30, Direction.L],
                                      '6': ['6', TuringState.q30, Direction.L],
                                      '7': ['7', TuringState.q30, Direction.L],
                                      '8': ['8', TuringState.q30, Direction.L],
                                      '9': ['9', TuringState.q30, Direction.L],
                                      '#': ['', None, None]
                    },
                    TuringState.q31: {'0': ['1', TuringState.q40, Direction.L], 
                                      '1': ['2', TuringState.q30, Direction.L],
                                      '2': ['3', TuringState.q30, Direction.L],
                                      '3': ['4', TuringState.q30, Direction.L],
                                      '4': ['5', TuringState.q30, Direction.L],
                                      '5': ['6', TuringState.q30, Direction.L],
                                      '6': ['7', TuringState.q30, Direction.L],
                                      '7': ['8', TuringState.q30, Direction.L],
                                      '8': ['9', TuringState.q30, Direction.L],
                                      '9': ['0', TuringState.q31, Direction.L],
                                      '#': ['1', None, None]
                    },
                    TuringState.q40: {'0': ['0', TuringState.q40, Direction.L], 
                                      '1': ['1', TuringState.q30, Direction.L],
                                      '2': ['2', TuringState.q30, Direction.L],
                                      '3': ['3', TuringState.q30, Direction.L],
                                      '4': ['4', TuringState.q30, Direction.L],
                                      '5': ['5', TuringState.q30, Direction.L],
                                      '6': ['6', TuringState.q30, Direction.L],
                                      '7': ['7', TuringState.q30, Direction.L],
                                      '8': ['8', TuringState.q30, Direction.L],
                                      '9': ['9', TuringState.q30, Direction.L],
                                      '#': ['', TuringState.qe, None]
                    },
                    TuringState.qe: {'0': ['', None, Direction.L], 
                                     '1': ['', None, Direction.L],
                                     '2': ['', None, Direction.L],
                                     '3': ['', None, Direction.L],
                                     '4': ['', None, Direction.L],
                                     '5': ['', None, Direction.L],
                                     '6': ['', None, Direction.L],
                                     '7': ['', None, Direction.L],
                                     '8': ['', None, Direction.L],
                                     '9': ['', None, Direction.L],
                                     '#': ['', None, None]
                    },
                  }

currentState = TuringState.q00
userInput = ""
output = ""

while(True):
  # get next input character from user
  readSymbol = str(input("Enter next symbol "))
  #if input is not in an alphabet, ignore it
  if(readSymbol not in Alphabet):
    print("Invalid symbol")
    continue
  #if input is theta, get next state and output symbol and write it to output string, then exit program
  if(readSymbol == '#'):
    nextOutputSymbol = transitionTable[currentState][readSymbol][0]
    nextState = transitionTable[currentState][readSymbol][1]
    nextDirection = transitionTable[currentState][readSymbol][2]
    output = nextOutputSymbol + output
    if nextState != None:
      currentState = nextState
    print(f"({readSymbol}, {currentState}, {nextOutputSymbol}, {nextState}, {nextDirection})")
    print(f"End of input reached. End state: {currentState} Output: {output} for given input: {userInput}")
    exit()

  #get next outputSymbol from the transition table
  nextOutputSymbol = transitionTable[currentState][readSymbol][0]
  #get next state from the transition table
  nextState = transitionTable[currentState][readSymbol][1]
  #get next direction from the transition table
  nextDirection = transitionTable[currentState][readSymbol][2]
  #print Turing Machine's function pass
  print(f"({readSymbol}, {currentState}, {nextOutputSymbol}, {nextState}, {nextDirection})")
  #write read symbol to saved user input string
  userInput = readSymbol + userInput
  #write output symbol to the output string
  output = nextOutputSymbol + output
  #set current Turing Machine's state
  currentState = nextState
