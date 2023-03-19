# python3

def parallel_processing(n, m, data):
    
    
    output = []
    tnumber = [0] * n
    
    for i in range (m):
        thread = 0
        for x in range (1, n):
            if tnumber[x]<tnumber[thread]
            thread = x
            start = tnumber[thread]
            end = start + data[i]
    
    return output

def main():
    
    
    n, m = map(int, input().split())
    
    if not (1 <= n <= 10**5):
        raise ValueError("n is not between 1 and 10^5")
        
    if not (1 <= m <= 10**5):
        raise ValueError("m is not between 1 and 10^5")
        
    data = list(map(int, input().split()))
    
    if len(data) != m:
        raise ValueError("data is not equal to m")
        
    for i in range(m):
        
        if not (0 <= data[i] <= 10**9):
            raise ValueError("all/some elements in data are not between 0 and 10^9")

    result = parallel_processing(n, m, data)
    
    for pair in result:
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()
