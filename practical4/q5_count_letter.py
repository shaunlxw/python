def count_letter(str, ch):
    if len(str) == 0:
        return 0
    elif len(ch) != 1:
        return "Enter one letter only!"
    elif str[0] == ch:
         return 1 + count_letter(str[1:], ch)
    else:
        return count_letter(str[1:],ch)
    
str = input("Enter text: ")
ch = input("Enter one letter: ")
print(count_letter(str,ch))
