from queue import Queue

def calc_faults(pages,n,capacity):
    frame = set()
    Q = Queue()
    pf = 0
    for i in range(n):
        if len(frame)<capacity:
            if pages[i] not in frame:
                frame.add(pages[i])
                pf+=1
                Q.put(pages[i])
        else:
            if pages[i] not in frame:
                val = Q.queue[0]
                Q.get()
                frame.remove(val)
                frame.add(pages[i])
                pf += 1
                Q.put(pages[i])

    return pf

if __name__=="__main__":
    print()
    ref_string = input()
    #pages = []
    for digit in ref_string:
        pages.append(int(digit))
    print(pages)
    capacity = int(input())
    n = len(ref_string)
    ans = calc_faults(pages,n,capacity)
    fr = (ans/n)*100
    print("Total faults: %d\t\tFault rate:%d\n"%(ans,fr));
