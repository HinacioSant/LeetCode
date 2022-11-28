# Problem 383. Ransom Note:

#  Given two strings ransomNote and magazine, return true if ransomNote
# can be constructed by using the letters from magazine and false
# otherwise.  Each letter in magazine can only be used once in
# ransomNote.

# Solution:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = list(ransomNote)
        b = list(magazine)
        while a != []:
            x = list(set(a).intersection(b))
            if x != []:
                for i in x:
                    a.remove(i)
                    b.remove(i)
            else:
                return False
        else:
            return True
