def isValid(str1):
    # st = []
    # for i in range(len(str1)):
    #     if (str1[i]=='[' or str1[i] == '{' or str1[i] == '('):
    #         st.append(str1[i])
    #     elif (str1[i] ==']' or str1[i]== '}' or str1[i] == ')'):
    #         st.pop(str1[i])
    #     elif ((str1[i] =='[' or str1[i] == '{' or str1[i]=='(') != (str1[i]==']' or str1[i] == '}' or str1[i] == ')' )):
    #         return False
    # if len(st)==0:
    #     return True
    # else:
    #     return False

    st = []
    for i in range(len(str1)):
        if str1[i] == '(' or str1[i] == '{' or str1[i] =='[':
            st.append(str1[i])
        elif str1[i] == ')' and (len(st) ==0 or st[-1] != '(') : return False
        elif str1[i] == '}' and (len(st) == 0 or st[-1] != '{') : return False
        elif str1[i] == ']' and (len(st) == 0 or st[-1] != '[') : return False
        else:
            st.pop()
    return len(st)==0
    # if len(st) == 0:
    #     return True
    # else:
    #     return False

def main():
    str1 = '()'
    print(isValid(str1))
main()
