

class Hash_set():
    def __init__(self, size= 20):
        self.size = size
        self.container = [ [] for _ in range(size)]

    def hash_func(self,value):
        sum = 0
        for ch in value:
            sum  += ord(ch)
        return (sum % self.size)

    def add(self, value):
        index =self.hash_func(value)
        bucket = self.container[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        index = self.hash_func(value)
        bucket = self.container[index]
        if value in bucket:
            return True
        
    def remove(self, value):
        index = self.hash_func(value)
        bucket = self.container[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        # Print all elements in the hash set
        print("Hash Set Contents:")
        for index, bucket in enumerate(self.container):
            print(f"Bucket {index}: {bucket}")     


# Creating the Hash Set from the simulation
hash_set = Hash_set(size=10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.print_set()

print("\n'Peter' is in the set:",hash_set.contains('Peter'))
print("Removing 'Peter'")
hash_set.remove('Peter')
print("'Peter' is in the set:",hash_set.contains('Peter'))
print("'Adele' has hash code:",hash_set.hash_func('Adele'))


