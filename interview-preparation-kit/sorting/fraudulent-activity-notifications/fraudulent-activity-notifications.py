def activityNotifications(expenditure, d):
    
    notifications = 0
    dataset = []
    median = 0

    for i in range(d, len(expenditure)):
        
        if i == d:

            # initial dataset
            dataset = sorted(expenditure[i-d:i])

        else:

            # remove first number from dataset
            first = expenditure[i-d-1]
            low, high = 0, d-1

            while low < high:
                mid = (low+high)//2
                if dataset[mid] < first: 
                    low = mid+1
                else: 
                    high = mid

            del dataset[low]

            # insert next number to dataset
            next = expenditure[i-1]
            low, high = 0, d-1

            while low < high:
                mid = (low+high)//2
                if next < dataset[mid]: 
                    high = mid
                else: 
                    low = mid+1

            dataset.insert(low, next)
            
        # find the median
        if d % 2 == 0: 
            median1 = dataset[d//2] 
            median2 = dataset[d//2 - 1] 
            median = (median1 + median2)/2
        else: 
            median = dataset[d//2] 

        # check if is greater than double median
        if expenditure[i] >= median * 2:
            notifications += 1

    return notifications

n, d = map(int, input().rstrip().split())

expenditure = list(map(int, input().rstrip().split()))

result = activityNotifications(expenditure, d)

print(result)