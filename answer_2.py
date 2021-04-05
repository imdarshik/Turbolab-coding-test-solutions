### Input strings
s1 = 'e#fee'
s2 = 'fe#fe'

def check_string_match(s1,s2):

    if len(s1) != len(s2):
        return 'DIFFERENT'

    else:

        if s1.count('e') > s2.count('e'):
            s1 = s1.replace('#','f')
            s2 = s2.replace('#','e')

        elif s1.count('f') > s2.count('f'):
            s1 = s1.replace('#','e')
            s2 = s2.replace('#','f')

        if s1 == s2:
            return 'MATCH'

        else:

            for i in range(len(s1)-1):
                if s1[i] != s2[i]:
                    s1 = list(s1)
                    t = s1[i]
                    s1[i] = s1[i+1]
                    s1[i+1] = t
                    s1 = ''.join(s1)

                if s1 == s2:
                    return 'MATCH'

            if s1 != s2:
                return "DIFFERENT"

print(check_string_match(s1,s2))