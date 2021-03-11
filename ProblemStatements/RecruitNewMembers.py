# Description : Suppose you are a manager as a big firm and now are looking for new members for your team. You sent out
# an advertisement and have received a few applications. You have a habit of scoring people on a scale of 100. You
# have given scores to all the members of your team and the new applications. The process of selection is going to be
# very straightforward if the applicant improves the average of the team then you hire the applicant to join the team
# or else reject the application. Remember the order of processing applications is going to be important here.
#
#
#
# You may see this as an extension of the previous problem, which it is. You may use the code written in the previous
# question as a function to improve the code quality.


# Take input here
# we will take input using ast sys
import ast

team = ast.literal_eval(input())
applicant = ast.literal_eval(input())


# Remember how we took input in the Alarm clock Question in previous Session?
# Lets see if you can finish taking input on your own

# start writing your code to find if check is above average of data
def check_sum(data, check):
    # sum = int(reduce(lambda x,y:x+y, data))
    s = sum(data)
    team_avg = s / len(data)
    if check > team_avg:
        return 1
    else:
        return 0


for i in applicant:
    is_add = check_sum(team, i)
    if is_add == 1:
        team.append(i)

print(team)
