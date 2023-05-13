import time



def calc_profit(investment):
    while True:
        profit = investment * 0.10
        investment += profit

        print(f"current balance: {investment}")
        time.sleep(24 * 60 * 60) #(24 * 60 * 60)
                        #hour, minutes, seconds

#initial investment
initial_investment = int(input("how much would you like to invest? "))


calc_profit(initial_investment)
