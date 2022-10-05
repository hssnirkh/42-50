def make_adder(x):
    def addfive():
        return x+5
    return addfive
result = make_adder(10)
print(result())
