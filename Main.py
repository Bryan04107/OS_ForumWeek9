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
    direction = -1
    scanMovement = 0

    if sorted == True:
        requests.sort()

    while requests:
        while initial_head in requests:
            requests.remove(initial_head)
        scanMovement += 1

        if initial_head == minRandom or initial_head == maxRandom:

            direction *= -1

        initial_head += direction
        
    return scanMovement - 1



def cscan(requests, initial_head, sorted):
    direction = -1
    cscanMovement = 0

    if sorted == True:
        requests.sort()

    while requests:
        while initial_head in requests:
            requests.remove(initial_head)
        cscanMovement += 1

        if initial_head == minRandom:
            initial_head = maxRandom -1
            cscanMovement += 4999

        initial_head += direction
        
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