import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

CLUE_START_IDX = [1, 5, 0, 4, 7, 4, 3, 0, 1, 4]
CLUE_END_IDX = [13, 12, 10, 12, 13, 14, 10, 11, 8, 15]
ANSWER_ROW = 7

def duration_to_int(duration: str) -> int:
    """ 
    Computes integer duration of string if format corresponds to X min

    Args:
        duration (str): the input duration string
    Returns:
        int: number of corresponding minutes
    """

    match = re.match(r"(\d+ ?)(?=min)", duration)
    if match:
        return int(match.group())
    else:
        return np.nan 
    
    
def add_column_duration_int(df: pd.DataFrame) -> pd.DataFrame:
    """ 
    Add a new column `duration_int` containing the duration as an integer
     to a dataframe with a previous column `duration`

    Args:
        df (pd.DataFrame): the input DataFrame
    Returns:
        df_new (pd.DataFrame): new dataframe with added `duration_int` column
    """

    # You will learn more about `apply` on later units
    df_new = df.copy()
    df_new["duration_int"] = df_new["duration"].apply(duration_to_int)
    return df_new


def draw_crosswords(text, colours):
    fig, ax = plt.subplots(figsize=(4,4))
    ax.axis('off')
    ax.axis('tight')
    ax.table(cellText=text, cellColours=colours, loc=(0,0), cellLoc='center')
    fig.tight_layout()
    plt.show()

def create_puzzle_colors():
    map_colors = np.full((np.max(CLUE_END_IDX),len(CLUE_START_IDX)), 'k', dtype=str)
    for i in range(len(CLUE_START_IDX)):
        map_colors[CLUE_START_IDX[i]:CLUE_END_IDX[i],i]='w'
    map_colors[ANSWER_ROW,:]='c'  
    map_colors = list(map_colors)
    map_colors = [list(row) for row in map_colors]
    return map_colors
    
def draw_base_puzzle():
    map_colors = create_puzzle_colors()
    n_cols = range(len(map_colors[0]))
    n_rows = range(len(map_colors))
    
    text = [["" for i in n_cols] for j in n_rows]
    draw_crosswords(text, map_colors)
    
def draw_final_puzzle(clues):
    map_colors = create_puzzle_colors()
    n_cols = range(len(map_colors[0]))
    n_rows = range(len(map_colors))
    
    text = [["" for i in n_cols] for j in n_rows]
    for col in n_cols:
        start_idx = CLUE_START_IDX[col]
        end_idx = CLUE_END_IDX[col]
        clue = clues[col]
        
        idx = 0
        for letter in clue:
            text[start_idx + idx][col] = clue[idx].upper()
            idx += 1 
            if start_idx + idx >= end_idx:
                break
        
    draw_crosswords(text, map_colors)
