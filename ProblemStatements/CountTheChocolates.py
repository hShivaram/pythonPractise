# Description : Sanjay loves chocolates. He goes to a shop to buy his favourite chocolate. There he notices there is an
# offer going on, upon bringing 3 wrappers of the same chocolate, you will get new chocolate for free. If Sanjay has
# m Rupees. How many chocolates will he be able to eat if each chocolate costs c Rupees?


# take input here
inp = input()
m_list = inp.split(",")
m = int(m_list[0])
c = int(m_list[1])

no_choc = m // c
no_wrapper = m // c

while no_wrapper // 3 != 0:
    no_choc = no_choc + no_wrapper // 3
    no_wrapper = no_wrapper // 3 + no_wrapper % 3

print(no_choc)

# start writing your code here


# dont forget to print the number of chocolates Sanjay can eat
