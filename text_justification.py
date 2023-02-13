class Solution:
    def make_line(self, words, line_words, line_length, max_width):
        #print(line_length, "LINE LENGTH")
        fillables = len(line_words) - 1
        real_line_length = (line_length - fillables) if fillables else line_length
        extra_spaces = max_width - line_length

        line = words[line_words[0]]
        if fillables:
            base_space = (max_width - real_line_length) // fillables
            extra_spaces = (max_width - real_line_length) % fillables
        else:
            return line + (" " * extra_spaces)    

        for i in range(1, len(line_words)):
            spaces = base_space
            if extra_spaces:
                spaces += 1
                extra_spaces -= 1

            line += (" " * spaces) + words[line_words[i]]

        return line




    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        lines = []

        i = 0
        words_to_process = len(words)

        
        line_words = []
        line_length = 0
        while i < words_to_process:
            cur_len = len(words[i])

            if not line_length:
                line_length = cur_len
            elif line_length + 1 + cur_len <= maxWidth:
                line_length += (1 + cur_len)
            else:
                # cant add more words, time to join.
                line = self.make_line(words, line_words, line_length, maxWidth)
                lines.append(line)
                
                line_words = []
                line_length = cur_len
                
            line_words.append(i)
            i += 1
            
        line = " ".join([words[i] for i in line_words])
        line += " " * (maxWidth - len(line))
        lines.append(line)

        return lines
