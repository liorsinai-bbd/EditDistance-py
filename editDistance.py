"""
Edit distance: the minimum number of transformations on characters to turn one string into another.
Valid transformations: remove, insert, replace

Reference
- https://en.wikipedia.org/wiki/Edit_distance, 
- https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm

Code from GeeksForGeeks: https://www.geeksforgeeks.org/edit-distance-dp-5/
Contributed by Bhavya Jain

Dynamic programming approach
Space Complexity: O(m*n)
Time Complexity:  O(m*n)
"""

NOTHING = -1
REPLACE = 0
INSERT = 1
REMOVE = 2

import sys

def _editDistanceDP(word1: str, word2:str): 
    m = len(word1)
    n = len(word2)
    # Create a table to store results of subproblems
    dp = [[0] * (n + 1) for x in range(m + 1)]
 
    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # If first string is empty, only option is to insert all characters of second string
            if i == 0:
                dp[i][j] = j   
 
            # If second string is empty, only option is to remove all characters of second string
            elif j == 0:
                dp[i][j] = i    

            # If last characters are same, ignore last char and recur for remaining string
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            # If last characters are different, consider all possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      # Insert
                                   dp[i-1][j],      # Remove
                                   dp[i-1][j-1])    # Replace

    return dp


def editDistance(word1: str, word2:str) -> int:
    """
    Calculate the Levenshtein edit distance between 2 words. 
    Allowable transforms per character: insert, remove, replace.

    E.g. editDistance(Hello, World) -> 4
    """
    m = len(word1)
    n = len(word2)
    dp = _editDistanceDP(word1, word2)
    return dp[m][n]

def argmin(arr):
    minpair = min(enumerate(arr), key=lambda x: x[1])
    return minpair[0]


def editPath(word1, word2):
    """
    Get the minimum edits to transform one word into another.
    Allowable transforms per character: insert, remove, replace.

    Edit pairs are (edit_type, current_cost) where edit type is an enum:

    NOTHING = -1
    REPLACE = 0
    INSERT = 1
    REMOVE = 2
    """
    dp = _editDistanceDP(word1, word2)
    i, j = len(word1), len(word2)
    path = [(NOTHING, dp[i][j])]
    while i > 0 or j > 0:
        if i == 0:
            while j > 0:
                path.append((INSERT, 1))
                j -= 1
        elif j == 0:
            while i > 0:
                path.append((REMOVE, 1))
                i -= 1
        elif word1[i - 1] == word2[j - 1]:
            path.append((NOTHING, 0))
            i -= 1
            j -= 1
        else:
            costs = [0, 0, 0] # replace, insert, remove
            costs[REPLACE] = dp[i - 1][j - 1] if ((i> 0) and (j > 0)) else float('inf')
            costs[INSERT]  = dp[i][j - 1] if ((j > 0)) else float('inf')
            costs[REMOVE]  = dp[i -1][j] if ((i > 0)) else float('inf')
            best_action = argmin(costs)
            if best_action == REPLACE:
                path.append((REPLACE, costs[REPLACE]))
                i -= 1
                j -= 1
            elif best_action == INSERT:
                path.append((INSERT, costs[INSERT]))
                j -= 1
            else: # elif best_action == REMOVE:
                path.append((REMOVE, costs[REMOVE]))
                i -= 1
    path.reverse()
    return path


def printEdits(editpath, word1, word2):
    """
    Print the minimum edits to transform one word to another.
    E.g. 

    Hello -> World
    edit distance: 4
    rp Hello -> Wello
    rp Wello -> Wollo
    rp Wollo -> Worlo
       Worlo -> Worlo
    rp Worlo -> World
    """
    action_sym = {REPLACE: "rp", REMOVE: "rm", INSERT: "in", NOTHING: "  "}
    i = 0 # index in oldstr

    newstr = word1
    for j, action_cost in enumerate(editpath[:-1]):
        action, cost = action_cost
        oldstr = newstr
        if action == NOTHING:
            newstr = oldstr
            newstr_print = oldstr[:i + 1] + '\u0332' + oldstr[i + 1:] # underline the working character
            action = NOTHING
            i += 1
        elif action == REMOVE:
            newstr = oldstr[:i] + oldstr[i + 1:]
            newstr_print = oldstr[:i] + "_" + oldstr[i + 1:]
        elif action == INSERT:
            newstr = oldstr[:i] + word2[i] + oldstr[i:]
            newstr_print = oldstr[:i] + word2[i] + '\u0332' +  oldstr[i:] # underline the working character
            i += 1
        else: # action == REPLACE:
            newstr = oldstr[:i] + word2[i] + oldstr[i + 1:]
            newstr_print = oldstr[:i] + word2[i] + '\u0332' + oldstr[i + 1:] # underline the working character
            i += 1

        oldstr = oldstr[:i] + '\u0332' + oldstr[i:] # underline the working character
        print(action_sym[action], "{0} -> {1}".format(oldstr, newstr_print))


def main(argv):
    #word1 = 'zzzzHEllooWurlld'  # kitten   AACAGTTACC  sunday     make this empty  zzzzHEllooWurlld
    #word2 = 'HelloWorld'  # sitting  TAAGGTCA    saturday   ''               HelloWorld 

    word1 = argv[1]
    word2 = argv[2] if len(argv) == 3 else ''

    print("{0} -> {1}".format(word1, word2))

    editpath = editPath(word1, word2)
    print("edit distance:", editpath[-1][1])

    printEdits(editpath, word1, word2)

if __name__ == '__main__':
    main(sys.argv)
    
