import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import yfinance as yf
import csv
import matplotlib.pyplot as plt

class Investment():

    def __init__(self):

        self.main()

    def main(self):

        grp1= ['buy', 'sell', 'price', 'help','exit','portfolio','graph']

        while True:

            act= input(f"{Style.BRIGHT}Select an action to perform (Buy/Sell/Price/Portfolio/Graph/Help/Exit): ").lower().strip()

            if act not in grp1:
                print(f"{Fore.RED}Select a valid action.")


            if act=='price':
                self.price()

            if act== 'buy':
                self.buy()

            if act=='sell':
                self.sell()

            if act=='exit':
                exit(f"Data Saved. Goodbye")

            if act== 'portfolio':
                self.portfolio()

            if act=='graph':
                self.graph()

            if act=='help':
                self.help()


    def buy(self):

        print(f"{Fore.BLUE}Use Help to look up some tickers.")
        print(f"{Fore.BLUE}All Prices are rounded off to the nearest integer.")

        try:
            stock1= input("Enter Stock Name you wish to purchase: ").strip().upper()

            cost= yf.Ticker(stock1)
            price1= cost.history(period='1d')["Close"].iloc[-1]
            print(f"${round(price1)} each")

        except IndexError:
            print(f"{Style.BRIGHT}{Fore.RED}Invalid Stock Name. You are being redirected")
            self.main()

        while True:
            try:

                num= int(input("How many?: "))
                if num<=0:
                    print(f"{Style.BRIGHT}{Fore.RED}Enter a positive integer.")

                elif num>1000:
                    print(f"{Fore.RED}{Style.BRIGHT}Cannot buy more than 1000 shares at once.")

                elif num>0:
                    break


            except ValueError:
                print(f"{Style.BRIGHT}{Fore.RED}Enter a positive integer")

        total= round(price1)*num

        print(f"Total cost is ${total}")

        while True:
            conf= input("Do you wish to complete the purchase? (Yes/No): ").lower().strip()

            if conf not in ['yes', 'no', 'y', 'n']:
                print(f"{Fore.RED}{Style.BRIGHT}invalid input. Enter Yes/No")

            else:
                break

        if conf in ['no', 'n']:
            print(f"{Fore.RED}Transaction Cancelled :(")

        elif conf in ['yes', 'y']:

            file= os.path.isfile("data.csv")


            if not file:
                with open("data.csv", 'a', newline='') as f:
                    writer= csv.DictWriter(f, fieldnames=['name', 'number', 'total cost'])
                    writer.writeheader()
                    writer.writerow({'name': stock1, 'number': num, 'total cost': total})

                print(f"{Fore.GREEN}Success :)")

            else:

                stocks= []

                with open("data.csv", 'r') as q:
                    reader= csv.DictReader(q)
                    for row in reader:
                        stocks.append(row)

                    exist=False
                    for i in stocks:
                        if i['name']==stock1:

                            new1= int(i['number'])+num
                            new2=int(i['total cost'])+total

                            i['number']=new1
                            i['total cost']=new2
                            exist=True
                            break

                    if not exist:

                            stocks.append({"name": stock1, "number": num, "total cost": total})

                    with open("data.csv", 'w', newline='') as e:

                        writer= csv.DictWriter(e, fieldnames= ['name', 'number', 'total cost'])
                        writer.writeheader()
                        for i in stocks:
                            writer.writerow(i)

                    print(f"{Style.BRIGHT}{Fore.GREEN}Success!")


    def price(self):

        print(f"{Fore.BLUE}Use Help to look up some tickers.")
        print(f"{Fore.BLUE}All prices are rounded off to the nearest integer.")

        try:
            stock1= input("Enter Stock Name: ").strip().upper()

            cost= yf.Ticker(stock1)
            price1= cost.history(period="1d")["Close"].iloc[-1]
            print(f"${round(price1)} each")

        except IndexError:
            print(f"{Style.BRIGHT}{Fore.RED}Invalid Stock Name. You are being redirected.")


        self.main()


    def sell(self):

        file= os.path.isfile('data.csv')

        if not file:
            print(f"{Style.BRIGHT}{Fore.RED}No STocks to Sell. You are being redirected.")
            self.main()

        print(f"{Fore.BLUE}Use Help to look up some tickers")

        try:
            stock1= input("Enter Stock Name you wish to sell: ").strip().upper()

            cost= yf.Ticker(stock1)
            price1= cost.history(period='1d')["Close"].iloc[-1]
            price2= round(price1)
            print(f"${price2} each")

        except IndexError:

            print(f"{Style.BRIGHT}{Fore.RED}Invalid Stock Name. You are being redirected.")
            self.main()

        stocks=[]

        with open("data.csv", 'r') as f:
            reader= csv.DictReader(f)
            for row in reader:
                stocks.append(row)

        found= False
        for i in stocks:

            if i['name']==stock1:

                found= True
                num2= int(i['number'])
                total2= int(i['total cost'])
                total= num2*price2

                while True:

                    conf= input(f"Do you wish to sell {num2} shares of {stock1} for a total of {total} (Yes/No): ").lower().strip()

                    if conf not in ['yes', 'no', 'y', 'n']:
                        print(f"{Fore.RED}{Style.BRIGHT}invalid input. Enter Yes/No")

                    else:
                        break

                if conf in ['no', 'n']:
                    print(f"{Fore.RED}Transaction Cancelled :(")
                    self.main()

                elif conf in ['yes', 'y']:

                    stocks.remove(i)
                    with open('data.csv', 'w', newline='') as q:
                        writer= csv.DictWriter(q, fieldnames=['name', 'number', 'total cost'])
                        writer.writeheader()

                        for j in stocks:
                            writer.writerow(j)

                        lp= total-total2

                        if lp>0:
                            print(f"{Fore.GREEN}{num2} shares of {stock1} sold at a profit of ${lp}")

                        if lp==0:
                            print(f"{Fore.YELLOW}{num2} shares of {stock1} sold at Buying Price. No Loss/Profit")

                        if lp<0:
                            print(f"{Fore.RED}{num2} shares of {stock1} sold at a loss of ${abs(lp)}")

                        break

        if not found:
            print(f"{Style.BRIGHT}{Fore.RED}Stock {stock1} not found in your portfolio.")

    def portfolio(self):

        file= os.path.isfile('data.csv')

        if not file:
            print(f"{Fore.RED}No Stocks to Display.")

        if file:

            with open("data.csv", 'r') as f:
                grp= f.readlines()
                for i in grp:
                    print(f"{Style.BRIGHT}{Fore.CYAN}{i}")

            print(f"You are being redirected.")

        self.main()


    def graph(self):

        name= input("Enter stock ticker: ").strip().upper()
        cost= yf.Ticker(name)
        data= cost.history(period='6mo')

        plt.figure(figsize= (10,5))

        plt.plot(data.index, data["Close"], label= f"{name} Closing Price")

        plt.title(f"{name} Stock Price (Last 6 months)")

        plt.xlabel("Date")

        plt.ylabel("Price (USD)")

        plt.legend()
        plt.grid(True)

        plt.show()
        
    def help(self):

        print(f"{Style.BRIGHT}{Fore.YELLOW}Here is what all the 'actions' do:")
        print("Buy= Buying Stocks")
        print("Sell: Selling Stocks")
        print("Price: CHeking price of a stock")
        print("Portfolio: Prints all stocks you own (with number and total value you bought them for)")
        print("Graph: Makes a graph of a stock (6 month history)")
        print("Help : Prints this :)")
        print("Exit: Exits the program (But data is saved)")
        print(f"{Style.BRIGHT}{Fore.YELLOW}Some common Stock tickers:")
        print("AAPL : Apple Inc.")
        print("MSFT : Microsoft Corporation")
        print("TSLA : Tesla, Inc.")
        print("AMZN : Amazon.com, Inc.")
        print("GOOGL : Alphabet Inc. (Google)")
        print("META : Meta Platforms, Inc. (Facebook)")
        print("NVDA : NVIDIA Corporation")
        print("NFLX : Netflix, Inc.")
        print("For a full list of tickers, visit:")
        print("https://stockanalysis.com/stocks/")


if __name__=="__main__":
    invest=Investment()
