transitionTable = [
        [
          "q00", [["0", ["3", "q10", "L"]], ["1", ["4", "q10", "L"]],
          ["2", ["5", "q10", "L"]], ["3", ["6", "q10", "L"]],
          ["4", ["7", "q10", "L"]], ["5", ["8", "q10", "L"]],
          ["6", ["9", "q10", "L"]], ["7", ["0", "q11", "L"]],
          ["8", ["1", "q11", "L"]], ["9", ["2", "q11", "L"]],
          ["#", ["", "qe", ""]]]
        ],
       [
         "q10", [["0", ["0", "q20", "L"]], ["1", ["1", "q20", "L"]],
         ["2", ["2", "q20", "L"]], ["3", ["3", "q20", "L"]],
         ["4", ["4", "q20", "L"]], ["5", ["5", "q20", "L"]],
         ["6", ["6", "q20", "L"]], ["7", ["7", "q20", "L"]],
         ["8", ["8", "q20", "L"]], ["9", ["9", "q20", "L"]],
         ["#", ["", "qe", ""]]]
       ],
       [
         "q11", [["0", ["1", "q20", "L"]], ["1", ["2", "q20", "L"]],
         ["2", ["3", "q20", "L"]], ["3", ["4", "q20", "L"]],
         ["4", ["5", "q20", "L"]], ["5", ["6", "q20", "L"]],
         ["6", ["7", "q20", "L"]], ["7", ["8", "q20", "L"]],
         ["8", ["9", "q20", "L"]], ["9", ["0", "q21", "L"]],
         ["#", ["", "qe", ""]]]
       ],
       [
         "q20", [["0", ["0", "q30", "L"]], ["1", ["1", "q30", "L"]],
          ["2", ["2", "q30", "L"]], ["3", ["3", "q30", "L"]],
          ["4", ["4", "q30", "L"]], ["5", ["5", "q30", "L"]],
          ["6", ["6", "q30", "L"]], ["7", ["7", "q30", "L"]],
          ["8", ["8", "q30", "L"]], ["9", ["9", "q30", "L"]],
          ["#", ["", "qe", ""]]]
       ],
       [
         "q21", [["0", ["1", "q30", "L"]], ["1", ["2", "q30", "L"]],
         ["2", ["3", "q30", "L"]], ["3", ["4", "q30", "L"]],
         ["4", ["5", "q30", "L"]], ["5", ["6", "q30", "L"]],
         ["6", ["7", "q30", "L"]], ["7", ["8", "q30", "L"]],
         ["8", ["9", "q30", "L"]], ["9", ["0", "q31", "L"]],
         ["#", ["", "qe", ""]]]
       ],
       [
         "q30", [["0", ["0", "q30", "L"]], ["1", ["1", "q30", "L"]],
         ["2", ["2", "q30", "L"]], ["3", ["3", "q30", "L"]],
         ["4", ["4", "q30", "L"]], ["5", ["5", "q30", "L"]],
         ["6", ["6", "q30", "L"]], ["7", ["7", "q30", "L"]],
         ["8", ["8", "q30", "L"]], ["9", ["9", "q30", "L"]],
         ["#", ["", "q30", ""]]]
       ],
       [
         "q31", [["0", ["1", "q30", "L"]], ["1", ["2", "q30", "L"]],
         ["2", ["3", "q30", "L"]], ["3", ["4", "q30", "L"]],
         ["4", ["5", "q30", "L"]], ["5", ["6", "q30", "L"]],
         ["6", ["7", "q30", "L"]], ["7", ["8", "q30", "L"]],
         ["8", ["9", "q30", "L"]], ["9", ["0", "q31", "L"]],
         ["#", ["1", "q30", ""]]]
       ],
       [
         "qe", [["0", ["1", "q30", "L"]], ["1", ["2", "q30", "L"]],
          ["2", ["3", "q30", "L"]], ["3", ["4", "q30", "L"]],
          ["4", ["5", "q30", "L"]], ["5", ["6", "q30", "L"]],
          ["6", ["7", "q30", "L"]], ["7", ["8", "q30", "L"]],
          ["8", ["9", "q30", "L"]], ["9", ["0", "q31", "L"]],
          ["#", ["", "qe", ""]]]
       ]]


def transitionFunction(currentState, inputSymbol):
    for transitionTableRow in transitionTable:
        if transitionTableRow[0] == currentState:
            for transitionTableSubRow in transitionTableRow[1]:
                if transitionTableSubRow[0] == inputSymbol:
                    return transitionTableSubRow[1]
    return None


while True:
    # stwórz tablicę na stany
    stateHistory = []
    # ustaw stan początkowy
    currentState = "q00"
    # pobierz ciąg znaków do sprawdzenia
    inputString = str(input("Enter symbols string: "))
    # obsługa pustego wejścia
    if len(inputString) < 1:
        print("Empty string was given")
        continue

    # pobranie indeksu znaku w ciągu, od którego rozpoczynamy czytanie
    # z racji ze czytamy od prawej do lewej, pobieramy indeks ostatniego znaku
    currSymbolIdx = len(inputString) - 1
    while True:
        if currSymbolIdx < 0:
            print(f"Output: {inputString}, end state: {currentState}, consecutive states: {stateHistory}")
            break
        elif currSymbolIdx > len(inputString) - 1:
            print("Index out of input string range")
            break

        inputChar = inputString[currSymbolIdx]
        transitionFunctionResult = transitionFunction(currentState, inputChar)
        if transitionFunctionResult is None:
            print(f"Symbol '{inputChar}' not found in transition table")
            break

        idxChange = 0
        if transitionFunctionResult[2] == 'L':
            idxChange = -1
        elif transitionFunctionResult[2] == 'R':
            idxChange = 1
        elif transitionFunctionResult[2] != '':
            print("Error in transition table - invalid Turing Machine head traverse direction")
            break

        if currSymbolIdx == len(inputString) - 1:
            inputString = inputString[:currSymbolIdx] + transitionFunctionResult[0]
        elif currSymbolIdx == 0:
            inputString = transitionFunctionResult[0] + inputString[1:]
        else:
            inputString = inputString[:currSymbolIdx] + transitionFunctionResult[0] + inputString[currSymbolIdx + 1:]
        print(f"Turing machine result: <{inputChar}, {currentState}, {transitionFunctionResult[0]}, {transitionFunctionResult[1]}, {transitionFunctionResult[2]}>")
        currSymbolIdx = currSymbolIdx + idxChange
        currentState = transitionFunctionResult[1]
        stateHistory.append(currentState)

        if idxChange == 0:
            print(f"Output: {inputString}, end state: {currentState}, consecutive states: {stateHistory}")
            break
