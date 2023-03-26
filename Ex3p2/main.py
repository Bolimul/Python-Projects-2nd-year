# Exercise 4 part 2
#Author: Nikita Solonets
#ID: 340961408
class node():
    '''
    This class represents an element of tree
    '''
    def __init__(self, number = 0):
        '''
        This constructor has a key value and empty list for nodes which the node object has
        :param number: key value for node
        '''
        self.entry = number
        self.node_list = []

    def __repr__(self):
        '''
        string representation for python
        :return: a string, which contains an info about the node
        '''
        if len(self.node_list) == 0:
            return f'<{self.entry}>;'
        return f'{self};'

    def __str__(self):
        '''
        string representation to print
        :return: a string, which contains an info about the node
        '''
        if len(self.node_list) == 0:
            return f'<{self.entry}>;'
        return f'<{self.entry}>{self.node_list.__str__()}'

    def insert(self, key):
        '''
        THis method represents an insertion of new node into existing tree
        :param key: key of new node
        :return: none if the tree already has the value
        '''
        if self.entry == key:
            return None
        else:
            if len(self.node_list) == 0:
                self.node_list.append(node(key))
            elif len(self.node_list) == 1:
                self.node_list.append(node(key))
                if key < self.entry:
                    self.node_list.sort(key=lambda x: x.entry, reverse=False)
            elif len(self.node_list) == 2:
                if self.entry < key:
                    self.node_list.append(node(key))
                elif self.entry > key:
                    if self.entry < self.node_list[1].entry:
                        self.node_list.append(node(key))
                        self.node_list.sort(key=lambda x: x.entry, reverse=False)
                    else:
                        av = (self.node_list[0].entry + self.node_list[1].entry) / 2
                        if key < av:
                            self.node_list[0].insert(key)
                        else:
                            self.node_list[1].insert(key)
            elif len(self.node_list) == 3:
                if self.entry < key:
                    self.node_list.append(node(key))
                    self.node_list.sort(key=lambda x: x.entry, reverse=False)
                elif self.entry > key:
                    if self.entry < self.node_list[1].entry:
                        self.node_list.append(node(key))
                        self.node_list.sort(key=lambda x: x.entry, reverse=False)
                    else:
                        av = (self.node_list[0].entry + self.node_list[1].entry) / 2
                        if key < av:
                            self.node_list[0].insert(key)
                        else:
                            self.node_list[1].insert(key)
            elif len(self.node_list) == 4:
                if key > self.entry:
                    av = (self.node_list[2].entry + self.node_list[3].entry)/2
                    if key < av:
                        self.node_list[2].insert(key)
                    else:
                        self.node_list[3].insert(key)
                elif key < self.entry:
                    av = (self.node_list[0].entry + self.node_list[1].entry)/2
                    if key < av:
                        self.node_list[0].insert(key)
                    else:
                        self.node_list[1].insert(key)

    def delete(self, node_to_delete):
        '''
        THis method represents a deletion of the node with specific key
        :param node_to_delete: key of node to delete from the tree
        :return: 1 if deletion is successful, none if it's not
        :raise: TreeIllegalValue exception if the node is not a leaf of the tree
        '''
        required_node_index = list(filter(lambda x:x if x.entry == node_to_delete else None, self.node_list))
        if len(required_node_index) == 0:
            required_node_index = None
        if required_node_index != None:
            required_node_index = self.node_list.index(required_node_index[0])
            if  self.node_list[required_node_index].entry == node_to_delete:
                    if len(self.node_list[required_node_index].node_list) == 0:
                        del self.node_list[required_node_index]
                        return 1
                    else:
                        raise TreeIllegalValue(node_to_delete)
        if len(self.node_list) == 1:
            return self.node_list[0].delete(node_to_delete)
        elif len(self.node_list) == 2:
            av = (self.node_list[0].entry + self.node_list[1].entry)/2
            if node_to_delete < av:
                return self.node_list[0].delete(node_to_delete)
            else:
                return self.node_list[1].delete(node_to_delete)
        elif len(self.node_list) == 3:
            if node_to_delete > self.entry:
                return self.node_list[2].delete(node_to_delete)
            else:
                av = (self.node_list[0].entry + self.node_list[1].entry)/2
                if node_to_delete < av:
                    return self.node_list[0].delete(node_to_delete)
                else:
                    return self.node_list[1].delete(node_to_delete)
        elif len(self.node_list) == 4:
            if node_to_delete > self.entry:
                av = (self.node_list[2].entry + self.node_list[3].entry)/2
                if node_to_delete < av:
                    return self.node_list[2].delete(node_to_delete)
                else:
                    return self.node_list[3].delete(node_to_delete)
            elif node_to_delete < self.entry:
                av = (self.node_list[0].entry + self.node_list[1].entry)/2
                if node_to_delete < av:
                    return self.node_list[0].delete(node_to_delete)
                else:
                   return self.node_list[1].delete(node_to_delete)
    def print(self):
        '''
        The function prints a whole tree
        :return: none because the function only executes
        '''
        print(f'{self}')

class TreeError(Exception):
    '''
    This class represents the errors in tree. Other classes with specific errors inherit from it
    '''
    pass

class TreeValueDoesNotExist(TreeError):
    '''
    This class represents ia error, when the node with the key does not exist
    '''
    def __init__(self, num):
        '''
        constructor to hold a key
        :param num: key of node
        '''
        self.value = num

class TreeIllegalValue(TreeError):
    '''
    this class represents an error, when the node isn't a leaf in tree
    '''
    def __init__(self, num):
        '''
        constructor to hold a key
        :param num: key of node
        '''
        self.value = num
BT = 1
while True:
    print('Menu:')
    print('1. Create a tree')
    print('2. Insert a value to the tree')
    print('3. Delete the value from the tree')
    print('4. Print the tree')
    print('5. Exit')
    try:
        choice_num = int(input('Enter an option number: '))
        if choice_num == 1:
            value_for_tree = int(input('Enter a value for new tree: '))
            BT = node(value_for_tree)
        elif choice_num == 2:
            if type(BT) != node:
                raise UnboundLocalError
            else:
                value_for_tree = int(input('Enter a value to insert to the tree: '))
                BT.insert(value_for_tree)
        elif choice_num == 3:
            if type(BT) != node:
                raise UnboundLocalError
            value_for_tree = int(input('Enter a value to delete from the tree: '))
            value_1 = BT.delete(value_for_tree)
            if value_1 is None:
                raise TreeValueDoesNotExist(value_for_tree)
        elif choice_num == 4:
            print(BT)
        elif choice_num == 5:
            print("Exit from the program")
            break
        else:
            raise UnboundLocalError
    except TreeError as err:
        if type(err) is TreeValueDoesNotExist:
            print(f"{err.value} does not exist in the tree, you'll be redirected to the main menu")
        else:
            print(f"{err.value} is illegal, you'll be redirected to the main menu")
    except UnboundLocalError:
        print('The symbol was not correct, try again')
    except Exception:
        print('General error, exit from the program')
        break





