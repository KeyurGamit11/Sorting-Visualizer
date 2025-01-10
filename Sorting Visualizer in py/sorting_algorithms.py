from draw import draw_list

def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if (lst[j] > lst[j + 1] and ascending) or (lst[j] < lst[j + 1] and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.RED, j + 1: draw_info.GREEN}, clear_bg=True)
                yield True  # Yield after every swap


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(1, len(lst)):
        current = lst[i]
        j = i - 1
        while j >= 0 and ((lst[j] > current and ascending) or (lst[j] < current and not ascending)):
            lst[j + 1] = lst[j]
            j -= 1
            draw_list(draw_info, {j: draw_info.RED, j + 1: draw_info.GREEN}, clear_bg=True)
            yield True
        lst[j + 1] = current
        draw_list(draw_info, {j + 1: draw_info.YELLOW}, clear_bg=True)
        yield True


def visualize_merge_sort(draw_info, ascending=True):
    lst = draw_info.lst
    yield from merge_sort(draw_info, lst, 0, len(lst), ascending)

def merge_sort(draw_info, lst, start, end, ascending=True):
    if start < end - 1:
        mid = (start + end) // 2
        yield from merge_sort(draw_info, lst, start, mid, ascending)
        yield from merge_sort(draw_info, lst, mid, end, ascending)
        yield from merge(draw_info, lst, start, mid, end, ascending)

def merge(draw_info, lst, start, mid, end, ascending):
    left = lst[start:mid]
    right = lst[mid:end]
    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if (left[i] <= right[j] and ascending) or (left[i] > right[j] and not ascending):
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1
        draw_list(draw_info, {k: draw_info.GREEN}, clear_bg=True)
        yield True

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
        draw_list(draw_info, {k: draw_info.YELLOW}, clear_bg=True)
        yield True

    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1
        draw_list(draw_info, {k: draw_info.YELLOW}, clear_bg=True)
        yield True
