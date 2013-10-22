ConsistentHashing
=================

Consistent hashing is a technique for distributing data keys to storage servers (nodes).




Need for Consistent Hashing :: 

Consistent hashing is a technique for distributing data keys to storage servers (nodes). Consistent hashing maps objects to the same cache machine, as far as possible. It means when a cache machine is added, it takes its share of objects from all the other cache machines and when it is removed, its objects are shared between the remaining machines. A common way of load balancing n cache machines is to put object o in cache machine number hash(o) mod n. But this will not work if a cache machine is added or removed because n changes and every object is hashed to a new location. Hence consistent hashing is needed to avoid swamping of servers.


The main idea behind the consistent hashing algorithm is to associate each cache with one or more hash value intervals where the interval boundaries are determined by calculating the hash of each cache identifier. The hash function used to define the intervals does not have to be the same function used to hash the cached values. Only the range of the two functions need match.



Implementation :: 

Defined a class named Consistent_Hashing(n,r) which creates a consistent hash object for n machines having r replicas. The class has a single instance method, get_machine(key), which returns the machine number to which the key is mapped. One function my_hash(key) is defined which returns a hash value of the key in the range [0,1). In class Consistent_Hashing, hash_tuples is a list of tuples (j, k, hash), where j ranges over machine numbers (0...n-1), k ranges over replicas (0...r-1), and hash is the corresponding hash value in the range [0,1).  The tuples are sorted by increasing hash value.



