# from node_ import Node
try:
    from linked_list_ import LinkedList, Node
except Exception:
    from .linked_list_ import LinkedList, Node

def merge_lists(list1, list2):
    """
    Merge two singly linked lists in place in 'zipper' fashion, alternating nodes from each of the given lists into the first list and vacating the second.
    """
    # try:
    list1_current = list1.head
    list2_current = list2.head

    while list1_current and list2_current:
        list1_next = list1_current.next_node
        list2_next = list2_current.next_node
        
        list1_current.next_node = list2_current

        if not list1_next:
            break

        list2_current.next_node = list1_next

        list1_current = list1_next
        list2_current = list2_next

    list2.head = None
    return list1
    # except:
    #     return "Error occurred while attempting the merge_lists method."

# BONUS TRACK - my (working) ll-reverse code from CC-09
def reverse_list(lst1):
    prev = None
    current = lst1.head
    next_ = current.next_node

    while current:
        current.next_node = prev
        prev = current
        current = next_
        try:
            next_ = current.next_node
        except AttributeError:
            pass
    lst1.head = prev

    return lst1




if __name__ == "__main__":
    print("Proof of Life")
    ll1 = LinkedList()
    lst1 = ll1.insert("kale")
    lst1 = ll1.insert("spinach")
    lst1 = ll1.insert("romaine")
    print("List 1: ", str(ll1))
    reverse_list(ll1)
    print("List 1: ", str(ll1))
    # ll2 = LinkedList()
    # # apples = ll.insert('apples')
    # # print(apples.value)
    # # ll.insert("apples")
    # # ll.insert("bananas")
    # # ll.insert("cantaloupes")
    # # ll.insert("d'Anjou pears")
    # # ll.insert_after("bananas", "limes")
    # # print(str(ll))
    # lst1 = ll1.insert("kale")
    # lst1 = ll1.insert("spinach")
    # lst1 = ll1.insert("romaine")
    # # lst1 = ll1
    # lst2 = ll2.insert("cucumber")
    # lst2 = ll2.insert("broccoli")
    # lst2 = ll2.insert("red bell peppers")
    # # lst2 = ll2
    # print("List 1: ", str(lst1))
    # print("List 2: ", str(lst2))
    # # merge_lists(lst1, lst2)
    # print(str(merge_lists(ll1, ll2)))
    # # print("Result: ", str(ll1))
