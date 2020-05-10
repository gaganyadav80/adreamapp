from First import best_day
#from api_link_data import count

count = 1
def fertilizer_time():
    start_day=best_day()

    output_file_1 = open("output_file_1.txt","w+")
    #output_file.write(str(max_profit))
    #output_file.write("\nabc")

    if(count == 1):
        output_file_1.write("Use fertilizer on first day. Use 4.5 KG fertilizer for 1 hectare of land.")

    elif(count >= 10):
        output_file_1.write("It's been 10 days. Use 3 KG fertilizer for 1 hectare of land.")

    elif(count>=25 and count<=30):
        output_file_1.write("It's been 25-30 days. Use 2.5 KG fertilizer for 1 hectare of land.")

    elif(count>=55 and count<=60):
        output_file_1.write("It's been 55-60 days. Use 1.25 KG fertilizer for 1 hectare of land.")

    elif(count>60):
        output_file_1.write("It's been more than 60 days. Please DO NOT use fertilizer now.")
