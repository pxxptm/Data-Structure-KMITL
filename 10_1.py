def bi_search(l, r, arr, x):

    now = int((l+r)/2)

    if l == r and arr[now] != x :
        return False

    if arr[now] == x :
        return True

    if arr[now] > x :
        return bi_search(l,now-1,arr,x)

    if arr[now] < x :
        return bi_search(now+1,r,arr,x)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))