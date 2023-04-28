# Bloom Filter

A Bloom filter is a probabilistic data structure that is used to test whether an element is a member of a set. It provides a space-efficient and fast mechanism for testing membership of elements, but with a small risk of false positives.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Bloom_filter.svg/360px-Bloom_filter.svg.png">
    <p>An example of a Bloom filter, representing the set {x, y, z} . The colored arrows show the positions in the bit array that each set element is mapped to. The element w is not in the set {x, y, z} , because it hashes to one bit-array position containing 0. For this figure, m = 18 and k = 3</p>
</div>

## How does it work?

A Bloom filter works by hashing an input element to produce a set of indexes in a bit array. The bits at these indexes are then set to 1. To test if an element is in the set, it is hashed to produce the same set of indexes, and the bits at those indexes are checked. If all of the bits are set to 1, then the element is probably in the set. However, if any of the bits are 0, then the element is definitely not in the set.

Since multiple elements can hash to the same set of indexes, false positives can occur. The probability of a false positive can be reduced by increasing the size of the bit array and the number of hash functions used.

## Applications

Bloom filters are used in a variety of applications, including data storage, networking, and database systems. They provide a space-efficient way to test for membership of large sets, and can be used in situations where the cost of false positives is low.

## Implementation

The `BloomFilter` class is placed here [bloom_filter.py](../../data_structures/bloom_filter.py)

## Explanation

The `BloomFilter` class takes two arguments in its constructor, the `capacity` and the `error rat`e. The `capacity` is the maximum number of elements that the filter can store, and the `error rate` is the probability that a test for an element in the set will return `true` even if the element is not actually in the set. The `capacity` and `error rate` are used to compute the number of hash functions that will be used to map elements to the bit array.

The `add` method takes an item as an argument and uses the `_hash_functions` method to compute a list of indices in the bit array corresponding to the item. The bits at those indices are then set to 1.

The `contains` method also takes an item as an argument and uses the `_hash_functions` method to compute a list of indices corresponding to the item. It then checks if all the bits at those indices in the bit array are 1 and returns `true` if they are and `false` otherwise.

The `TestBloomFilter` class defines test cases for the `BloomFilter` class. The `setUp` method creates an instance of the `BloomFilter` class with a `capacity` of 10 and an `error rate` of 0.1, which is used for all the test cases. The `test_add` method tests the `add` method by adding three items to the filter and checking if they are all in the filter. The `test_contains` method tests the `contains` method by adding three items to the filter, checking if they are in the filter and checking if two items that were not added to the filter are not in the filter.