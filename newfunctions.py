# obtain last line
# def final_line(file):
#     lines = file.read().splitlines()
#     last_line = lines[-1]
#     return(last_line)


# # obtain final wave split
# def final_wave_split(file):
#     Final_Wave = wave_split.split()[1]
#     Final_Wave_Clean = Final_Wave.replace(",", " ")
#     Wave_As_Int = int(Final_Wave_Clean)
#     print("Your most recent wave split:", Wave_As_Int)

# def success_or_fail(file):
#     last_line = final_line(file)
#     if "Duration (Failed): " in last_line:
#         fail_counter += 1
#     elif "Duration (Success): " in last_line:
#         success_counter += 1