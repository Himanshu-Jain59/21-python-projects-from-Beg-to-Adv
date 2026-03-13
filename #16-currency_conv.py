import requests 

BASE_URL="https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies"

def get_rates(from_curr,to_curr):
    try:
        data = requests.get(f"{BASE_URL}/{from_curr.lower()}.min.json",timeout=5).json()[from_curr.lower()][to_curr.lower()]
        print(f"1 {from_curr} = {round(data,3)} {to_curr}")
        return round(data,3)
    except requests.exceptions.RequestException:
        print("Network error.Check your internet.")
        return None
    except KeyError:
        print("Conversion Not Available")
        return None

def convert (ex_rates,from_curr,to_curr,amount):
        return amount*ex_rates
        

def main():
    print("=== Currency Converter ===")
    while True:
        from_curr=input("From currency (e.g. INR): ").upper()
        to_curr=input("To currency (e.g. USD): ").upper()
        try:
            amount=float(input("Enter amount to convert: "))
        except:
             print("Invalid amount")
             continue
        
        ex_rates = get_rates(from_curr,to_curr)
        if ex_rates:
            res = convert(ex_rates,from_curr,to_curr,amount)
            print(f"{amount} {from_curr} = {res} {to_curr}")
        again = input("convert again(y/n): ").lower()
        if again!="y":
             break
        
if __name__ =="__main__":
    main()

        