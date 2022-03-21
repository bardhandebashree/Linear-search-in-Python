# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def linear_search(arr, k):
    flag = 0
    c = 0
    l = [0 for i in range(5)]


    length = len(arr)
    for i in range(0, length - 1, 1):

        
        if k == arr[i]:
            flag = 1
            print(c)
            l[c] = i
            c = c + 1
    if flag == 1:
        print("Found in")
        print(l)
    else:
        print("Not Found")



    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [3, 45, 67, 67, 67]
    print(arr)
    k = int(input(':input number to be searched'))
    linear_search(arr, k)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
