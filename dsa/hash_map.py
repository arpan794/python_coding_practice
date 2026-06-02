class Hash_map():
    def __init__(self, size= 20):
        self.size = size
        self.container = [ [] for _ in range(size)]

    def hash_func(self,value):
        sum = 0
        for ch in value:
            sum  += ord(ch)
        return (sum % self.size)

    def put(self, key, value):
        index =self.hash_func(key)
        bucket = self.container[index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self.hash_func(key)
        bucket = self.container[index]
        for k,v in bucket:
            if k == key:
                return v
        return None
        
    def remove(self, key):
        index = self.hash_func(key)
        bucket = self.container[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  
                return

    def print_map(self):
        # Print all elements in the hash set
        print("Hash map Contents:")
        for index, bucket in enumerate(self.container):
            print(f"Bucket {index}: {bucket}")     




hash_map = Hash_map(size=10)

# Adding some entries
hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.put("123-4672", "Adele")
hash_map.put("123-4573", "Michaela")
hash_map.put("123-6574", "Bob")

hash_map.print_map()

# Demonstrating retrieval
print("\nName associated with '123-4570':", hash_map.get("123-4570"))

print("Updating the name for '123-4570' to 'James'")
hash_map.put("123-4570","James")

# Checking if Peter is still there
print("Name associated with '123-4570':", hash_map.get("123-4570"))