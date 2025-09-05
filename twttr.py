# user = input('enter word: ')
# list1 = ['a','A', 'e', 'E', 'o', 'O', 'u', 'U', 'i', 'I']
# new_str = ''
# for x in user:
#     if x not in list1:
#         new_str += x

# print(new_str)

def shorten(word):

    v_list = ['a','A', 'e', 'E', 'o', 'O', 'u', 'U', 'i', 'I']
    output_str = ''
    for x in word:
        if x not in v_list:
            output_str += x

    return output_str


def main():
    text = input("Input: ")
    print("Output:", shorten(text))


if __name__ == "__main__":
    main()
