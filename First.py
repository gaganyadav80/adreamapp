import time
import pandas as pd
import math
from datetime import date
import datetime

def best_day():
    dt = datetime.datetime.today()

    df = pd.read_excel("temp_data.xlsx","Sheet1")
    #print(df['dates'][91])


    if(dt.month==11):
        i =dt.day-1
        no_of_days=30
    if(dt.month==12):
        i=dt.day+30
        no_of_days=31
    #print(i)
    profit = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    j=i+40
    k=0
    #print(j)
    #print(df['dates'][j])
    for i in range(i,i+14):
        #print(i)
        for j in range(i+40,i+54):
            #print(j)
            #print("hello")
            #print(k)
            #print("hello")
            #print(df['dates'][j+40])
            if (df['max'][j]<33 and df['max'][j]>30):
                profit[k]=profit[k]+1
            if (df['max'][j]>33):
                greater=33-df['max'][j]
                greater=greater/100
                #print(greater)
                profit[k]=profit[k]+math.exp(greater)
            if (df['max'][j]<30):
                lesser=df['max'][j]-30
                lesser=lesser/100
                #print(lesser)
                profit[k]=profit[k]+math.exp(lesser)
        k=k+1

        #print(profit[i])
    '''
        def bubble_sort(nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    # Swap the elements
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    # Set the flag to True so we'll loop again
                    swapped = True


    # Verify it works
    bubble_sort(profit)

    print(random_list_of_nums)
    '''
    max_date=dt.day
    max_profit=profit[0]
    for i in range(14):
        #print(profit[i])
        #max_profit=profit[0]
        #max_date=dt.day
        if(profit[i]>max_profit):
            max_profit=profit[i]
            value=i
            #print(i)
    #print(value)
    max_date=max_date+value
    if(max_date>no_of_days):
        max_date=max_date-no_of_days

    profit[value]=0.0

    #print("test")
    max_date_1=dt.day
    max_profit_1=profit[0]
    for t in range(14):
        #print(profit[t])
        #max_profit_1=profit[0]max_profit_1=profit[0]
        #max_date_1=dt.day
        if(profit[t]>max_profit_1):
            max_profit_1=profit[t]
            value=t
    #        #print(i)
    #print(max_date_1)
    #print(i)
    #print(value)
    max_date_1=max_date_1+value
    if(max_date_1>no_of_days):
        max_date_1=max_date_1-no_of_days
    #print(max_date_1)

    #print(max_profit)
    #print(max_profit_1)
    print(max_date)
    print(max_date_1)
    output_file= open("output_file.txt","w+")
    #output_file.write(str(max_profit))
    output_file.write(str(max_date))
    output_file.write(" And ")
    output_file.write(str(max_date_1))
    output_file.write(" are the most favorable days for seed plantat ")
    return(max_date)
