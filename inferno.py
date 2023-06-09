import os, datetime
from collections import Counter
# folder path for inferno stats txt file locations
# add own folder path here where txt files are saved
folder_path = ""


# Get a list of all files in the folder
file_list = os.listdir(folder_path)

# fail count 
fail_counter = 0
# success count
success_counter = 0
# list to store each runs wave checkpoint
Waves = []
Time_Of_Run = []

# Iterate over each file in the folder
for file_name in file_list:
    # Check if the file is a text file
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_path, file_name)
        
        # Open the file and read its contents
        with open(file_path, "r") as file:
            # split the lines up and assign it to lines variable
            lines = file.read().splitlines()
            # final line of the txt file (duration failed/success time)
            last_line = lines[-1]

            # add try/except here incase a run is less than a wave split (aka you died too fast)
            try:
                # assign the 2nd to last line to wave_split
                wave_split = lines[-2]
            except:
                # if no wave split print the error message
                print("You died too fast")
            
            # prints the time of clear / fail and then the last wave split reached
            print(last_line)

            Final_Time = last_line.split()[2]
            if "Success" not in last_line:
                print("You died at: " + Final_Time)
            else:
                print("You cleared the run at: " + Final_Time)
            print(wave_split)

            # obtain wave of death from the list
            Final_Wave = wave_split.split()[1]
            Final_Wave_Clean = Final_Wave.replace(","," ")
            Wave_As_Int = int(Final_Wave_Clean)
            print("Your most recent wave split:", Wave_As_Int)

            # time of file creation
            c_time = os.path.getctime(file_path)
            # convert creation timestamp into DateTime object
            dt_c = datetime.datetime.fromtimestamp(c_time)
            # make this more readable


            print("Date of run:",dt_c)

            # add wave split to list
            Waves.append(Wave_As_Int)
            print("\n")

            # convert the minutes to seconds
            Minutes_In_Seconds = (int(Final_Time[:2]) * 60) + (int(Final_Time[-2:]))
            # add the time to the list
            Time_Of_Run.append(Minutes_In_Seconds)

            # if failed run increase fail counter
            if "Duration (Failed): " in last_line:
                fail_counter+= 1

            # if successsful run increase success counter
            elif "Duration (Success): " in last_line:
                success_counter+= 1

        # Print the contents (this prints all aspects of the file read)
        # print(f"File: {file_name}\n{contents}\n")

print("Failed Runs:",fail_counter)
print("Successful Runs:",success_counter)
# add counter for number of runs dying "too fast" ?

# combine success and fail to get the total
total_runs = fail_counter + success_counter

# round the number to 2 decimal places
roundedNumber = round(success_counter/total_runs*100, 2)
print("Conversion Rate:",roundedNumber,"%")

# find the average wave, this only takes your "wave" as the wave split so isn't very accurate
Average_Wave = (sum(Waves))/(len(Waves))
print("Average Wave:",round(Average_Wave))

# find the most common wave split occurance
def Most_Common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]
print("The most common wave split reached:",Most_Common(Waves))

# average time of run in seconds
Average_RunTime_Seconds = (sum(Time_Of_Run))/(len(Time_Of_Run))
# convert the seconds to minute format to make it more readable
Average_RunTime = Average_RunTime_Seconds / 60
# convert number to string, get the first two numbers (the minutes which are before the colon)
Average_RunTime_Minutes = str(Average_RunTime)[:2]
# get the numbers after the colon (the seconds)
Average_RunTime_Seconds = str(Average_RunTime)[3:6]
# round the decimal point and find the seconds, convert to int so you can use it
Find_Remaining_Seconds = round((int(Average_RunTime_Seconds) / 1000) * 60)
# convert the seconds back to string
Seconds = str(Find_Remaining_Seconds)
print("Average time of run: " + Average_RunTime_Minutes + ":" + Seconds )

