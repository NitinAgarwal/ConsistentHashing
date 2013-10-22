
import bisect
import hashlib

class Consistent_Hashing:
	"""Consistent_Hashing(n,r) creates a consistent hash object for n machines having r replicas. """
	
	def __init__(self, num_machines=1, num_replicas=1):
		self.num_machines = num_machines
		self.num_replicas = num_replicas
		
		hash_tuples = [(j, k, my_hash(str(j)+"_"+str(k))) \
						for j in range(self.num_machines) \
						for k in range(self.num_replicas)]
    	
    	# Sort the hash tuples based on just the hash values
		hash_tuples.sort(lambda x,y: cmp(x[2],y[2]))
		self.hash_tuples = hash_tuples


	def get_machine(self, key):
		"""Returns the number of the machine which key gets sent to. """
		h = my_hash(key)
		
		# edge case where it cycle the past hash value of 1 and back to 0.
		if h > self.hash_tuples[-1][2]: 
			return self.hash_tuples[0][0]
		
		hash_values = map(lambda x: x[2], self.hash_tuples)
		index = bisect.bisect_left(hash_values, h)
		
		return self.hash_tuples[index][0]


def my_hash(key):
	""" returns a hash of the key in the range [0,1) """
	return (int(hashlib.md5(key).hexdigest(), 16) % 1000000)/1000000.0


def main():
	print "Enter the number of Machines" 
	num_machines = int(raw_input())

	print "Enter the number of Replicas"
	num_replicas = int(raw_input())

	ch = Consistent_Hashing(num_machines, num_replicas)
	print "(machine, replica, hash value):"
	for (j,k,h) in ch.hash_tuples: 
		print "(%s, %s, %s)" % (j, k, h)

	while True:
		print "\nPlease enter a key, or (a) to add machine:"
		key = str(raw_input())
		if key == 'a':
			print "New Hash Has Been Alloted"
			ch = Consistent_Hashing(num_machines+1, num_replicas)
			for (j,k,h) in ch.hash_tuples: 
				print "(%s, %s, %s)" % (j, k, h)
			num_machines = num_machines + 1
		else:	
			print "hash(Key: %s) = %s, Goes to machine %s" % (key, my_hash(key), ch.get_machine(key))
	

if __name__ == "__main__": 
	main()


