def shift_rows(state):
    for i in range(4):
        state[i] = state[i][i:] + state[i][:i]
    return state

