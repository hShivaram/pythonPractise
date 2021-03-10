# inp=input()
# m_list=inp.split(",")
# m=int(m_list[0])
# c=int(m_list[1])

# no_choc=m//c
# no_wrapper=m//c

# while(no_wrapper//3 !=0):
#    no_choc=no_choc + no_wrapper//3
#    no_wrapper=no_wrapper//3 + no_wrapper%3

# print(no_choc)
inp = input()
m_list = inp.split(",")
print(m_list)
total_money = int(m_list[0])
cost_choc = int(m_list[1])
free_choc = int(m_list[2])
wrapper = int(m_list[3])

no_choc = total_money // cost_choc
no_wrap = total_money // cost_choc
print(no_choc, no_wrap)
while (no_wrap // wrapper != 0):
    # print("c")
    no_choc = no_choc + free_choc
    no_wrap = no_wrap // wrapper + no_wrap % wrapper

print(no_choc)
