nfa = {}
paths = input("Enter the transition paths: ")
for i in input("Enter the states: "):
  nfa.update({i: {j: "" for j in paths}})
states = nfa.keys()
for state in states:
  for path in paths:
    nfa[state][path] = (input("Enter the end state from "+state+" through path "+path+": "))
dfa = nfa.copy()
for state in states:
  for path in paths:
    if nfa[state][path] not in states: dfa.update({nfa[state][path]: {i: "" for i in paths}})
for state in dfa.keys():
  if state not in states:
    for j in paths:
      endState = ""
      for i in state: 
        for k in nfa[i][j]:
          if k not in endState: endState += k
      dfa[state][j] = endState
print(nfa)
print(dfa)