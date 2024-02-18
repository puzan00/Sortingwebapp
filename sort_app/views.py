from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def bubble_sort(request):
    sorted_list = None
    error_message = None

    if request.method == "POST":
        unsorted_list_str = request.POST.get("unsorted_list", "")

        if unsorted_list_str:
            unsorted_list = list(map(int, unsorted_list_str.split(",")))
            n = len(unsorted_list)

            # Bubble Sort Algorithm
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if unsorted_list[j] > unsorted_list[j + 1]:
                        unsorted_list[j], unsorted_list[j + 1] = (
                            unsorted_list[j + 1],
                            unsorted_list[j],
                        )

            sorted_list = unsorted_list
        else:
            error_message = "Please enter a valid list of integers."

    return render(
        request,
        "bubble_sort.html",
        {"sorted_list": sorted_list, "error_message": error_message},
    )


def selection_sort(request):
    sorted_list = None
    error_message = None

    if request.method == "POST":
        unsorted_list_str = request.POST.get("unsorted_list", "")
        if unsorted_list_str:
            unsorted_list = list(map(int, unsorted_list_str.split(",")))
            n = len(unsorted_list)
            # Selection Sort Algorithm
            for i in range(n):
                min_index = i
                for j in range(i + 1, n):
                    if unsorted_list[j] < unsorted_list[min_index]:
                        min_index = j
                unsorted_list[i], unsorted_list[min_index] = (
                    unsorted_list[min_index],
                    unsorted_list[i],
                )
            sorted_list = unsorted_list
        else:
            error_message = "Please enter a valid list of integers."

    return render(
        request,
        "selection_sort.html",
        {"sorted_list": sorted_list, "error_message": error_message},
    )


def insertion_sort(request):
    sorted_list = None
    error_message = None

    if request.method == "POST":
        unsorted_list_str = request.POST.get("unsorted_list", "")
        if unsorted_list_str:
            unsorted_list = list(map(int, unsorted_list_str.split(",")))
            n = len(unsorted_list)

            # Insertion Sort Algorithm
            for i in range(1, n):
                key = unsorted_list[i]
                j = i - 1
                while j >= 0 and key < unsorted_list[j]:
                    unsorted_list[j + 1] = unsorted_list[j]
                    j -= 1
                unsorted_list[j + 1] = key

            sorted_list = unsorted_list
        else:
            error_message = "Please enter a valid list of integers."
    return render(
        request,
        "insertion_sort.html",
        {"sorted_list": sorted_list, "error_message": error_message},
    )
