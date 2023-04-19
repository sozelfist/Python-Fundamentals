# Bloom Filter

## Implementation

The `BloomFilter` class is placed here [bloom_filter.py](../../data_structures/bloom_filter.py)

## Explanation

This code defines a Bloom filter data structure, which is a probabilistic data structure that can be used to test whether an element is a member of a set. The basic idea behind a Bloom filter is that it uses a bit array to store information about a set of elements, and a number of hash functions to map elements to positions in the bit array. When an element is added to the set, the hash functions are used to compute a set of indices in the bit array, and the bits at those indices are set to 1. To test whether an element is in the set, the same hash functions are used to compute a set of indices, and if all of the bits at those indices are 1, then the element is considered to be in the set.

The `BloomFilter` class takes two arguments in its constructor, the `capacity` and the `error rat`e. The `capacity` is the maximum number of elements that the filter can store, and the `error rate` is the probability that a test for an element in the set will return `true` even if the element is not actually in the set. The `capacity` and `error rate` are used to compute the number of hash functions that will be used to map elements to the bit array.

The `add` method takes an item as an argument and uses the `_hash_functions` method to compute a list of indices in the bit array corresponding to the item. The bits at those indices are then set to 1.

The `contains` method also takes an item as an argument and uses the `_hash_functions` method to compute a list of indices corresponding to the item. It then checks if all the bits at those indices in the bit array are 1 and returns `true` if they are and `false` otherwise.

The `TestBloomFilter` class defines test cases for the `BloomFilter` class. The `setUp` method creates an instance of the `BloomFilter` class with a `capacity` of 10 and an `error rate` of 0.1, which is used for all the test cases. The `test_add` method tests the `add` method by adding three items to the filter and checking if they are all in the filter. The `test_contains` method tests the `contains` method by adding three items to the filter, checking if they are in the filter and checking if two items that were not added to the filter are not in the filter.