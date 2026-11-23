# NAME  : Harshith G
# USN   : 25BTRAD040
# BRANCH: CSE – AIDE A
# MINI PROJECT (UNIT 3) - Problem Solving Component
# Program 6: Sales Data Analyzer (Lists and Dictionaries)

# Data structure: dictionary -> {product: {"quantity": int, "price": float}}

def add_or_update_product(sales, product, quantity, price):
    """Add a new product, or update quantity/price of an existing one."""
    if quantity < 0 or price < 0:
        print("  Quantity and price cannot be negative.")
        return
    if product in sales:
        sales[product]["quantity"] += quantity   # add to units sold
        sales[product]["price"] = price          # latest price
        print(f"  Updated '{product}': qty={sales[product]['quantity']}, "
              f"price={price}")
    else:
        sales[product] = {"quantity": quantity, "price": price}
        print(f"  Added '{product}': qty={quantity}, price={price}")


def product_revenue(sales):
    """Return dictionary {product: revenue}."""
    return {p: d["quantity"] * d["price"] for p, d in sales.items()}


def total_sales(sales):
    return sum(product_revenue(sales).values())


def highest_selling(sales):
    """Highest-selling product by quantity sold."""
    if not sales:
        return None
    return max(sales, key=lambda p: sales[p]["quantity"])


def top_revenue_product(sales):
    revenue = product_revenue(sales)
    return max(revenue, key=revenue.get) if revenue else None


def summarize(sales):
    """Product-wise performance summary with share of total revenue."""
    revenue = product_revenue(sales)
    total = total_sales(sales)
    print("\n  {:<12} {:>5} {:>8} {:>10} {:>7}".format(
        "Product", "Qty", "Price", "Revenue", "Share"))
    print("  " + "-" * 46)
    # sorted from best to worst revenue (comparison of performance)
    for p in sorted(revenue, key=revenue.get, reverse=True):
        share = revenue[p] / total * 100 if total else 0
        print("  {:<12} {:>5} {:>8.2f} {:>10.2f} {:>6.1f}%".format(
            p, sales[p]["quantity"], sales[p]["price"], revenue[p], share))
    print("  " + "-" * 46)
    print("  {:<12} {:>5} {:>8} {:>10.2f}".format(
        "TOTAL", sum(d["quantity"] for d in sales.values()), "", total))


def test_sales():
    print("\n" + "=" * 50)
    print("PART 2: SALES DATA ANALYZER")
    print("=" * 50)

    # Dataset 1: normal data
    print("\n[Dataset 1] Normal data")
    sales = {}
    for p, q, pr in [("Pen", 120, 10), ("Notebook", 60, 45),
                     ("Bag", 15, 500), ("Marker", 80, 25)]:
        add_or_update_product(sales, p, q, pr)
    summarize(sales)
    print(f"\n  Highest-selling (by quantity): {highest_selling(sales)}")
    print(f"  Highest revenue product      : {top_revenue_product(sales)}")
    print("  Interpretation: Pen sells the most units, but Bag earns the "
          "most revenue because of its high price.")

    # Dataset 2: update + invalid input
    print("\n[Dataset 2] Updating records / invalid input")
    add_or_update_product(sales, "Pen", 30, 12)       # update
    add_or_update_product(sales, "Eraser", -5, 3)     # invalid
    summarize(sales)

    # Dataset 3: one product dominates
    print("\n[Dataset 3] One dominant product")
    s2 = {}
    add_or_update_product(s2, "Laptop", 10, 50000)
    add_or_update_product(s2, "Mouse", 200, 400)
    summarize(s2)
    print(f"\n  Highest-selling (by quantity): {highest_selling(s2)}")
    print(f"  Highest revenue product      : {top_revenue_product(s2)}")
    print("  Interpretation: Mouse sells more units, yet Laptop generates "
          "most of the revenue.")

    # Dataset 4: empty data
    print("\n[Dataset 4] Empty dataset")
    s3 = {}
    print(f"  Total sales: {total_sales(s3)}")
    print(f"  Highest-selling: {highest_selling(s3)}")


if __name__ == "__main__":
    test_sales()
