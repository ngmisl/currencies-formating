VAT = 0.20

# use cents
PRICES = {
    "burger":999,
    "fries":499,
    "drink": 199,
    "salad": 1499,
}

def order(items: list[str]):
    total = sum(PRICES[item] for item in items)
    vat = total * VAT
    total += vat
    print(f"Your order is ${total/100:.2f} (VAT: ${vat/100:2f}).") # use format/100:2.f for decimals
    print("Thanks for your business")
    
def main():
    order(["burger", "drink", "salad"])

if __name__ == "__main__":
    main()