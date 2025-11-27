class Solution:
    def romanToInt(self, s: str) -> int:
        dict_= {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
               }
        str_ = 0
        flag = True
        for i in range(len(s)):
            if not flag:
                flag = True
                continue
            try:
                if s[i] == "I":
                    if s[i+1] in ['V','X']:
                        if s[i+1] == 'V':
                            str_ += 4
                            flag = False
                        if s[i+1] == 'X':
                            str_ += 9
                            flag = False
                    else:
                        str_ += dict_.get(s[i])
                elif s[i] == 'X':
                    if s[i+1] in ['L','C']:
                        if s[i+1] == 'L':
                            str_ += 40
                            flag = False
                        if s[i+1] == 'C':
                            str_ += 90
                            flag = False
                    else:
                        str_+=dict_.get(s[i])
                elif s[i] == 'C':
                    if s[i+1] in ['D','M']:
                        if s[i + 1] == 'D':
                            str_ += 400
                            flag = False
                        if s[i + 1] == 'M':
                            str_ += 900
                            flag = False
                    else:
                        str_ += dict_.get(s[i])
                else:
                    str_ += dict_.get(s[i])
            except:
                str_ += dict_.get(s[i])

        return str_