# Calls the main function, which calls the other functions and declares/initializes variables.
def main():
    #Holds the information for the lists.
    First_name = ['John', 'Jake', 'Sally', 'Tou', 'Jacquelyn', 'John']
    Last_name = ['Johnson', 'Michaelson', 'weber', 'Xiong', 'Jackson', 'White']
    ID = ['895645', '236598', '225584', '364875', '984587', '560258']
    Grade = ['A', 'A', 'C', 'B', 'D', 'C']
# This calls print_record with an argument that is a list of indices, and all lists.
    print_Record(search_Record(First_name, Last_name, ID, Grade),First_name, Last_name, ID, Grade)

# Defines the print_record function.
def print_Record(Found_records,First_name, Last_name, ID, Grade):
    print("There are " ,len(Found_records), " records found")
    print("First_name".ljust(10, ' '), "Last_name".ljust(10, ' '), "ID".ljust(10, ' '), "Grade".ljust(10, ' '))
    print("".center(40, '='))
# Takes the indexes and outputs their full data entry via a list of indices.
    for x in Found_records:
        print(First_name[x].ljust(10, ' '), Last_name[x].ljust(10, ' '), ID[x].ljust(10, ' '),  Grade[x].ljust(10, ' '))
        
# Defines the search_record function,
# First it asks for user input and compares it to list names with if else statements.
# And compares the second user input with list values, then returns a list of indices.
# I was going to put the while loops in a seperate function called parser for cleaner code, that would be called in each if else statements,
# but was worried it would not fit the criteria/scope of this assignemnt.
def search_Record(First_name, Last_name, ID, Grade):
    Found_records = []
    search_type = input("Type to search: ")
# This matches user search type with existing lists.
    if search_type.casefold() == ("firstname").casefold():
        keyword = input("Keyword to search: ")
        i = 0
        while i < len(First_name):
# This matches users keyword with existing data entries.
# The casefold is used to make input case insensitive.
            if keyword.casefold() == First_name[i].casefold():
                Found_records.append(i)
                i+=1
            else:
                i+=1
        return Found_records
    elif search_type.casefold() == ("lastname").casefold():
        keyword = input("Keyword to search: ")
        i = 0
        while i < len(Last_name):
            if keyword.casefold() == Last_name[i].casefold():
                Found_records.append(i)
                i+=1
            else:
                i+=1
        return Found_records
    elif search_type.casefold() == ("id").casefold():
        keyword = input("Keyword to search: ")
        i = 0
        while i < len(ID):
            if keyword.casefold() == ID[i].casefold():
                Found_records.append(i)
                i+=1
            else:
                i+=1
        return Found_records
    elif search_type.casefold() == ("grade").casefold():
        keyword = input("Keyword to search: ")
        i = 0
        while i < len(Grade):
            if keyword.casefold() == Grade[i].casefold():
                Found_records.append(i)
                i+=1
            else:
                i+=1
        return Found_records
    else:
        print("wrong input")

main()
