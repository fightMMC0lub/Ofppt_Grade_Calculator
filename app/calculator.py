def calc_comm(french: float, arabic: float, english: float) -> float:
  
    return (2 * french + arabic + english) / 3

def calc_final(
    passage: float,
    modules: float,
    theory: float,
    practice: float,
    french: float,
    arabic: float,
    english: float
) -> float:

    comm = calc_comm(french, arabic, english)
    return (passage + 2 * modules + 2 * theory + 4 * practice + comm) / 10
