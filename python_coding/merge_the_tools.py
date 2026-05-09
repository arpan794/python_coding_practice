# Split the string into subsegments of length $k$, then print each subsegment with any duplicate characters stripped out.

def merge_the_tools(string, k):

    for i in range(0, len(string), k):

        segment = string[i:i+k]

        seen = set()
        result = ""

        for ch in segment:

            if ch not in seen:
                seen.add(ch)
                result += ch

        print(result)

  

    


merge_the_tools(string="aarpannan", k=3)