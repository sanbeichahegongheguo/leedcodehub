from add_two_numbers import *

if __name__ == '__main__':
    list01 = ListNode(2)
    list01.next = ListNode(4)
    list01.next.next = ListNode(4)
    list02 = ListNode(5)
    list02.next = ListNode(4)
    list02.next.next = ListNode(6)

    s1 = Solution()
    a = s1.addTwoNumbers(list01, list02)
    result = []
    while a is not None:
        print(a.val, end=" ")
        result.append(a.val)
        a = a.next
    print("")
    print(result)
