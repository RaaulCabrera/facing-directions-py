import os


def check_facing_direction(rows, cols):
    rows_is_odd = rows % 2 == 1
    cols_is_odd = cols % 2 == 1

    if not cols_is_odd and rows > cols:
        return "U"
    elif rows_is_odd and cols >= rows:
        return "R"
    elif not rows_is_odd and not cols_is_odd and cols >= rows:
        return "L"
    elif rows > cols and rows_is_odd and cols_is_odd:
        return "D"
    else:
        return "~:" + str(rows) + "x" + str(cols)


def main():
    if not os.path.exists('input.txt'):
        print("Please provide an input.txt")
        return
    output = open('output.txt', 'w')

    with open('input.txt', 'r') as file_input:
        inpt = file_input.readlines()
    
    header = inpt[0].rstrip('\n')

    if int(header) + 1 != len(inpt):
        print("File format is wrong")
        return
    
    for rows_cols in inpt[1:]:
        rows = int(rows_cols[0])
        cols = int(rows_cols[2])
        direction = check_facing_direction(rows, cols)
        print(str(rows) +"x" + str(cols) + "=" + direction)
        output.write(direction + "\n")
    output.close()

if __name__ == '__main__':
    main()