# python3

def parallel_processing(n, m, data):
    
    output = []
    tnumber = [0] * n
    
    for i in range(m):
        thread = 0
        for x in range(1, n):
            if tnumber[x] < tnumber[thread]:
                thread = x
        start = tnumber[thread]
        end = start + data[i]
        output.append((thread, start))
        tnumber[thread] = end
    
    return output

def main():
    
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)
    
    for pair in result:
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()
