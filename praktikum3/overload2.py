class dlvstudio:
    def __init__(self, fare):
        self.fare = fare

    def __add__(self, other):
        return self.fare+other.fare

ring = dlvstudio(5000)
keychain = dlvstudio(15000)
total = ring+keychain
print(f'\nHarga Total: {str(total)}\n')