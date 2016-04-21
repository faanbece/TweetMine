import fileinput
import glob

file_list = glob.glob('../Record/*.data')

with open('../result.data', 'w') as file:
    input_lines = fileinput.input(file_list)
    file.writelines(input_lines)
