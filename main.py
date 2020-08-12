# Imports
import os, math

# Setup file...
filesetup = open("recent.txt", 'w') # Open the file and write a header to it.
filesetup.write("[DATA FROM LAST OPERATION]")
filesetup.close()

recent = open("recent.txt", 'a') # Re-open the file for appending.

"""WINDOW"""
class window:
    # Setup window...
    def resize_window(self):
        cmd = 'mode 64,28'
        os.system(cmd)

    # Clear screen...
    def cls(self):
        os.system('cls' if os.name == 'nt' else "printf '\033c'") # Clear the screen

    # Set title...
    def set_header(self):
        os.system("title "+"StatisticCalculator")


# Instantiate a window
win = window()
win.resize_window()
win.cls()
win.set_header()

"""CALCULATOR FUNCTIONALITY"""
class functions:
    # Find mean.
    def mean(self):
        count = 0
        nums = []
        print("CALCULATE MEAN OF:")
        recent.write("\nCALCULATE MEAN OF:")
        while True:
            inp = input("\n")
            if inp == "done":
                mean = 0
                for num in nums:
                    mean += num
                try:
                    mean = mean/count
                except:
                    print("EMPTY LIST")
                    recent.write("EMPTY LIST")
                    break
                print("MEAN RESULT: " + str(mean))
                recent.write("MEAN RESULT: " + str(mean))
                break
            else:
                count += 1
                nums.append(float(inp))
                recent.write("\n" + inp)
                continue
    
    # Find median.
    def median(self):
        nums = []
        print("CALCULATE MEDIAN OF:")
        recent.write("\nCALCULATE MEDIAN OF:")
        while True:
            inp = input("\n")
            if inp == "done":
                nums.sort()
                middle = float(len(nums))/2
                try:
                    if middle % 2 != 0: # Return the center value if there is one.
                        mid = nums[int(middle - .5)]
                        print("MEDIAN RESULT: " + str(mid))
                        recent.write("MEDIAN RESULT: " + str(mid))
                    else: # Return the center two values' mean if there is an even number of values.
                        mid1 = nums[int(middle)]
                        mid2 = nums[int(middle-1)]
                        mid = (mid1+mid2)/2
                        print("MEDIAN RESULT: " + str(mid))
                        recent.write("MEDIAN RESULT: " + str(mid))
                    break
                except:
                    print("EMPTY LIST")
                    recent.write("EMPTY LIST")
                    break
                    
            else:
                nums.append(float(inp))
                recent.write("\n" + inp)
                continue
    
    # Find modal value.
    def modal(self):
        nums = []
        print("CALCULATE MODAL OF:")
        recent.write("\nCALCULATE MODAL OF:")
        while True:
            inp = input("\n")
            if inp == "done":
                nums.sort()
                counter = 0

                try:
                    num = nums[0]
                except:
                    print("EMPTY LIST")
                    recent.write("EMPTY LIST")
                    break

                for i in nums: 
                    curr_frequency = nums.count(i) 
                    if(curr_frequency> counter): 
                        counter = curr_frequency 
                        num = i 

                print("MODAL RESULT: " + str(num))
                recent.write("MODAL RESULT: " + str(num))
                
                break
            else:
                nums.append(float(inp))
                recent.write("\n" + inp)
                continue
    
    # Find modal value.
    def log(self):
        print("CALCULATE LOG OF:")
        recent.write("\nCALCULATE LOG OF:")
        inp = input("\n")
        try:
            num = math.log(float(inp))
            print("LOG RESULT: " + str(num))
            recent.write("LOG RESULT: " + str(num))
        except:
            print("EMPTY LIST")
            recent.write("EMPTY LIST")
    
    # Find range fancy.
    def fancy_range(self):
        count = 0
        nums = []
        print("CALCULATE RANGE OF:")
        recent.write("\nCALCULATE RANGE OF:")
        while True:
            inp = input("\n")
            if inp == "done":
                try:
                    nums.sort()
                    mn = min(nums)
                    mx = max(nums)
                    final = mx - mn
                except:
                    print("EMPTY LIST")
                    recent.write("EMPTY LIST")
                    break
                print("RANGE RESULT: " + str(final))
                recent.write("RANGE RESULT: " + str(final))
                break
            else:
                count += 1
                nums.append(float(inp))
                recent.write("\n" + inp)
                continue
    
    # Find range normal.
    def range(self, list):
        list.sort()
        mn = min(list)
        mx = max(list)
        final = mx - mn
        return final
    
    # Find standard deviation.
    def standard_deviation(self):
        count = 0
        nums = []
        print("CALCULATE STANDARD DEVIATION OF:")
        recent.write("\nCALCULATE STANDARD DEVIATION OF:")
        while True:
            inp = input("\n")
            if inp == "done":
                if len(nums) > 0:
                    # GET THE MEAN
                    mean = 0
                    for num in nums:
                        mean += num
                    mean = mean/count
                    # GET THE DEVIATIONS
                    deviations = []
                    for i in nums:
                        j = i - mean
                        deviations.append(j)
                    # SQUARE THE DEVIATIONS
                    squared_deviations = []
                    for i in deviations:
                        j = i ** 2
                        squared_deviations.append(j)
                    # FIND THE VARIANCE
                    num = 0
                    for i in squared_deviations:
                        num += i
                    varience = (num/len(squared_deviations))
                    # GET THE STANDARD DEVIATION
                    result = math.sqrt(varience)

                    print("STANDARD DEVIATION RESULT: " + str(result))
                    recent.write("STANDARD DEVIATION RESULT: " + str(result))
                    break
                else:
                    print("EMPTY LIST")
                    recent.write("EMPTY LIST")
                    break
            else:
                count += 1
                nums.append(float(inp))
                recent.write("\n" + inp)
                continue


# Instantiate functions
funcs = functions()
while True:
    inp = input("\n> ")
    recent.write("\n" + inp)
    if inp == "done":
        break
    elif inp == "mean":
        funcs.mean()
    elif inp == "median":
        funcs.median()
    elif inp == "mode" or inp == "modal":
        funcs.modal()
    elif inp == "log":
        funcs.log()
    elif inp == "range":
        funcs.fancy_range()
    elif inp == "sd" or inp == "standard deviation":
        funcs.standard_deviation()
    elif inp == "help":
        print("\nCOMMANDS\nhelp | shows this list\nmean | calculate the mean of a list\nmedian | calculate the median of a list\nmode | calculate the mode of a list\nlog | calculate a log with a base of ten\nrange | calculate the range of a list of numbers\nsd | calculate the standard deviation of a list\ndone | finish functions or end program")


input("Press 'Esc' to quit... ") # Stop the window from closing when tasks are complete, instead wait for the user to close the window.
recent.close() # Close the file.