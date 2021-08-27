"""
The Knuth-Morris-Pratt algorithm is a useful search algorithmn that finds substrings of text within body of text (or string)

The algorithm works by efficiently iterating through a given text. The algorithm uses the properties of the "Longest Prefix Suffix"
To accurately calculate the minimal index positioning at all times as it traverses the text_str.

This algorithm takes a pattern and a text. Although it requires foreknowledge of the length of the pattern and text_str 
*(though most modern programming languages keep track of this information for us).

The most important function is the computeLPS() function. This function finds the longest Prefix Suffix in a pattern. 

"""

def computeLPS(pattern,M,LPS_arr):
    l = 0
    i = 1
    LPS_arr[0] = 0

    while i < M:
        if(pattern[i] == pattern[l]):
            LPS_arr[i] = l + 1
            l += 1
            i += 1
        else:
            if l !=0:
                l = LPS_arr[l - 1]
            else:
                LPS_arr[i] = 0
                i += 1



def KMPsearch(pattern_str, text_str):
    n = len(text_str)
    m = len(pattern_str)
    lps = [0]*m
    computeLPS(pattern_str, m, lps)

    i = j = 0

    while i < n - m + 1:
        if(text_str[i] == pattern_str[j]):
            i += 1
            j += 1
        else:
            if (j != 0):
                j = lps[j - 1]
            else:
                i += 1
        if ( j == m):
            print( i - j)
            j = lps[j - 1]


