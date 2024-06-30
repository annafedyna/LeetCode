def strStr(haystack: str, needle: str) -> int:

    pointer1, pointer2 = 0, 0

    while pointer2 < len(needle) and pointer1 < len(haystack):
        if haystack[pointer1] == needle[pointer2]:
            pointer1 += 1
            pointer2 += 1
        else:
            pointer1 = pointer1 - pointer2 + 1
            pointer2 = 0

    return pointer1 - pointer2 if pointer2 == len(needle) else -1


print(strStr(haystack="mississippi", needle="issip"))
