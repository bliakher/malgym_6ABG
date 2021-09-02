# solution using only the data needed --------------------------

def sort_input():
	N = int(input())
	present = set()
	for i in range(N):
		input()
		K = int(input())
		for j in range(K):
			present.add(input())
	print_set(present)
	
def print_set(set):
	for i in set:
		print(i)

sort_input()

# solution creating child - presents dictionary first -----------

def get_presents() -> dict:
    """
    Function for getting dictionary of all presents

    :return: dictionary of child: list of presents
    """
    child_int = int(input('Number of letters: '))
    present_dict = {}
    
    for child in range(child_int):
        child_name = input('Child name: ')
        present_int = int(input('Number of presents: '))
        
        present_list = []  # reset list for each child
        for present in range(present_int):  # get the presents
            present_list.append(input('Present: '))
        
        present_dict[child_name] = present_list  # assign presents to a child
    
    return present_dict


def print_presents(present_dict: dict):
    """
    Function for printing all presents to be created

    :p_dict: dictionary of all children and presents;
             key: child, value: list of child's presents
    """
    present_set = set()  # set of all presents
    
    for present_list in present_dict.values():
        for present in present_list:
            present_set.add(present)  # add present to the set; if it is already there nothing happens

    print('\nOutput:')
    for present in present_set:
        print('-', present)  # print present


