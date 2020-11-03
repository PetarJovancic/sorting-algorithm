from datetime import datetime

class ReadData:
    """
    Reading data from the .txt
    """
    def __init__(self,filename):
        self.filename=filename

    def read_data(self):
        with open(self.filename, "r") as f:
            self.row_1 = f.readline()
            self.row_2 = f.readline()
            self.row_3 = f.readline()
        self.row_1 = self.row_1.rstrip("\n")
        self.row_2  = self.row_2 .rstrip("\n")
        self.row_3= self.row_3.rstrip("\n")
        return self.row_1, self.row_2, self.row_3

class FormatData:
    """
    Formatting data before sorting
    """

    """
    :returns converted string to list
    """
    @staticmethod
    def convert_str_to_list(comma,pipe,space):
        converted_comma=list(comma.split(", "))
        converted_pipe= list(pipe.split(" | "))
        converted_space=list(space.split(" "))
        return converted_comma, converted_pipe, converted_space

    """
    :returns reordered list
    """
    @staticmethod
    def reorder_list(row_1,row_2,row_3,order):
        row_1 = [row_1[i] for i in order]
        row_2 = [row_2[i] for i in order]
        row_3 = [row_3[i] for i in order]
        return row_1, row_2, row_3

    """
    :returns lists without middle name
    """
    @staticmethod
    def remove_middle_name(row_1,row_2,row_3):
        row_1.pop()
        row_2.pop()
        row_3.pop()
        return row_1,row_2,row_3

    """
    :returns lists with "F" and "M" converted to "Female" and "Male"
    """
    @staticmethod
    def convert_gender(row_1,row_2,row_3,g,gender):
        row_1_list=[]
        row_2_list = []
        row_3_list = []
        for string in row_1:
            new_string_1 = string.replace(g, gender)
            row_1_list.append(new_string_1)
        for string in row_2:
            new_string_2 = string.replace(g, gender)
            row_2_list.append(new_string_2)
        for string in row_3:
            new_string_3 = string.replace(g, gender)
            row_3_list.append(new_string_3)
        return row_1_list, row_2_list, row_3_list

    """
    :returns converted date in mm/dd/yyyy format
    """
    @staticmethod
    def convert_date(row_1_list,row_2_list,row_3_list):
        oldformat = row_1_list[3]
        datetimeobject = datetime.strptime(oldformat, '%m-%d-%Y')
        newformat2 = datetimeobject.strftime('%m/%d/%Y')
        row_1_list = [w.replace(oldformat, newformat2) for w in row_1_list]
        oldformat = row_2_list[3]
        datetimeobject = datetime.strptime(oldformat, '%m-%d-%Y')
        newformat2 = datetimeobject.strftime('%m/%d/%Y')
        row_2_list = [w.replace(oldformat, newformat2) for w in row_2_list]
        oldformat = row_3_list[3]
        datetimeobject = datetime.strptime(oldformat, '%m-%d-%Y')
        newformat2 = datetimeobject.strftime('%m/%d/%Y')
        row_3_list = [w.replace(oldformat, newformat2) for w in row_3_list]
        return row_1_list, row_2_list, row_3_list

    """
    :returns final formatted list
    """
    @staticmethod
    def append_list(comma_list_row_1,comma_list_row_2,comma_list_row_3,pipe_list_row_1,pipe_list_row_2,
                    pipe_list_row_3, space_list_row_1, space_list_row_2, space_list_row_3):
        final_list=[]
        final_list.append(comma_list_row_1)
        final_list.append(comma_list_row_2)
        final_list.append(comma_list_row_3)
        final_list.append(pipe_list_row_1)
        final_list.append(pipe_list_row_2)
        final_list.append(pipe_list_row_3)
        final_list.append(space_list_row_1)
        final_list.append(space_list_row_2)
        final_list.append(space_list_row_3)
        return final_list

def main():
    comma_str_row_1,comma_str_row_2,comma_str_row_3=ReadData("comma.txt",).read_data()
    pipe_str_row_1,pipe_str_row_2,pipe_str_row_3=ReadData("pipe.txt",).read_data()
    space_str_row_1,space_str_row_2,space_str_row_3=ReadData("space.txt",).read_data()

    comma_list_row_1,pipe_list_row_1,space_list_row_1=FormatData().convert_str_to_list(comma_str_row_1,pipe_str_row_1,space_str_row_1)
    comma_list_row_2,pipe_list_row_2,space_list_row_2=FormatData().convert_str_to_list(comma_str_row_2,pipe_str_row_2,space_str_row_2)
    comma_list_row_3,pipe_list_row_3,space_list_row_3=FormatData().convert_str_to_list(comma_str_row_3,pipe_str_row_3,space_str_row_3)

    order_comma = [0, 1, 2, 4, 3]
    order_pipe = [0, 1, 3, 5, 4, 2]
    order_space = [0, 1, 3, 4, 5, 2]

    comma_list_row_1,comma_list_row_2,comma_list_row_3=FormatData().reorder_list(comma_list_row_1,comma_list_row_2,comma_list_row_3,order_comma)
    pipe_list_row_1, pipe_list_row_2, pipe_list_row_3=FormatData().reorder_list(pipe_list_row_1, pipe_list_row_2, pipe_list_row_3, order_pipe)
    space_list_row_1, space_list_row_2, space_list_row_3=FormatData().reorder_list(space_list_row_1, space_list_row_2, space_list_row_3, order_space)

    pipe_list_row_1, pipe_list_row_2, pipe_list_row_3=FormatData().remove_middle_name(pipe_list_row_1, pipe_list_row_2, pipe_list_row_3)
    space_list_row_1, space_list_row_2, space_list_row_3=FormatData().remove_middle_name(space_list_row_1, space_list_row_2, space_list_row_3)

    pipe_list_row_1, pipe_list_row_2, pipe_list_row_3=FormatData().convert_gender(pipe_list_row_1,pipe_list_row_2,pipe_list_row_3,"M","Male")
    space_list_row_1, space_list_row_2, space_list_row_3=FormatData().convert_gender(space_list_row_1, space_list_row_2, space_list_row_3,"F","Female")

    pipe_list_row_1, pipe_list_row_2, pipe_list_row_3=FormatData().convert_date(pipe_list_row_1, pipe_list_row_2, pipe_list_row_3)
    space_list_row_1, space_list_row_2, space_list_row_3 = FormatData().convert_date(space_list_row_1, space_list_row_2, space_list_row_3)

    final_list=FormatData().append_list(comma_list_row_1,comma_list_row_2,comma_list_row_3,pipe_list_row_1,pipe_list_row_2, pipe_list_row_3, space_list_row_1, space_list_row_2, space_list_row_3)
    return final_list

if __name__=="__main__":
    main()