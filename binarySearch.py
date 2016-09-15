primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
          67, 71, 73, 79, 83, 89, 97]

def binarySearch(arr, target):
    lo = 0
    hi = len(arr) - 1
    while(lo<hi):
        mid = (lo+hi)//2
        print("High:", hi, "Low:", lo, "Mid:", mid, "Arr Mid", arr[mid])
        if (arr[mid] == target or lo = target or hi = target):
            print(target, "Found")
            return
        elif (arr[mid] > target):
            hi = mid - 1
        else:
            lo = mid + 1
    print("not found")
            
        



binarySearch(primes, 29)



