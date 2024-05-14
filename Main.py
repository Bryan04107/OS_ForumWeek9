maxRange = 1000
minRandom = 0
maxRandom = 4999



def fcfs(requests, initial_head, sorted):
    fcfsMovement = 0

    if sorted == True:
        if abs(initial_head - max(requests)) >= abs(initial_head - min(requests)):
            requests.sort()
        else:
            requests.sort(reverse=True)

    for request in requests:
        fcfsMovement += abs(request - initial_head)
        initial_head = request

    return fcfsMovement



def scan(requests, initial_head, sorted):
    scanMovement = 0
    head = initial_head

    if sorted == True:
        requests.sort()

    while requests:
        next_request = next((r for r in requests if r >= head), None)
        if next_request:
            scanMovement += next_request - head
            head = next_request
            requests.remove(next_request)
        else:
            scanMovement += maxRandom - head
            head = 0

    return scanMovement



def cscan(requests, initial_head, sorted):
    cscanMovement = 0
    head = initial_head

    if sorted == True:
        requests.sort()

    while requests:
        next_request = next((r for r in requests if r >= head), None)
        if next_request:
            cscanMovement += next_request - head
            head = next_request
            requests.remove(next_request)
        else:
            cscanMovement += maxRandom - head + maxRandom
            head = 0

    return cscanMovement



def main():
    import sys

    if len(sys.argv) != 3:
        print("Usage: python", sys.argv[0], "<initial_head> <request_file>")
        exit(1)

    initial_head = int(sys.argv[1])
    request_file = sys.argv[2]

    requests = []
    with open(request_file, 'r') as f:
        for line in f:
            requests.append(int(line.strip()))

    print("\nFCFS Total Head Movement:", fcfs(requests, initial_head, False))
    print("SCAN Total Head Movement:", scan(requests.copy(), initial_head, False))
    print("CSCAN Total Head Movement:", cscan(requests.copy(), initial_head, False))
    print("\nFCFS Optimized Total Head Movement:", fcfs(requests.copy(), initial_head, True))
    print("SCAN Optimized Total Head Movement:", scan(requests.copy(), initial_head, True))
    print("CSCAN Optimized Total Head Movement:", cscan(requests.copy(), initial_head, True))
    print("\n")



if __name__ == "__main__":
    main()