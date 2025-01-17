# Data Structures and Algorithms

## Language: `Python`

## Table of Contents of READMEs:
- [Code Challenge 1](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/codechallenge6/python/code_challenges/array-reverse)
- [Code Challenge 2](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/codechallenge6/python/code_challenges/list-insert-shift)
- [Code Challenge 3](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/codechallenge6/python/code_challenges/list-binary-search)
- Code Challenge 4 - no link
- [Code Challenge 5](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/codechallenge6/python/docs/READMEs/linked_list)
- [Code Challenge 6](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/codechallenge6/python/docs/READMEs/linked_list)
- [Code Challenge 7](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/linked-list-kth/python/docs/READMEs/linked_list)
- [Code Challenge 8](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/zip-lists/python/docs/READMEs/linked_list)
- [Code Challenge 10](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/stack-and-queue/python/docs/READMEs/stacks_and_queues)
- [Code Challenge 11](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/stack-queue-pseudo/python/docs/READMEs/pseudo_queue)
- [Code Challenge 12](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/stack-queue-animal-shelter/python/docs/stack_queue_animal_shelter)
- [Code Challenge 13](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/blob/stack-queue-brackets/python/docs/READMEs/stack-brackets/README.md)
- [Code Challenge 15](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/trees/python/docs/READMEs/binary_trees)
- [Code Challenge 16](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/tree-max/python/docs/READMEs/binary_trees)
- [Code Challenge 17](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/tree-breadth-first/python/docs/READMEs/breadth_first_tree)
- [Code Challenge 18](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/tree-fizz-buzz/python/docs/READMEs/fizzbuzz)
- [Code Challenge 26](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/insertion_sort/sorting/insertion)
- [Code Challenge 27](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/mergesort/sorting/merge)
- [Code Challenge 28](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/movie_sort/sorting/movie_sort)
- [Code Challenge 30](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/hashtable/python/docs/READMEs/Hashtables)
- [Code Challenge 31](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/hashmap-repeated-word/python/docs/hashtable_repeated_word)
- [Code Challenge 32](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/intersect/python/docs/tree_intersection)
- [Code Challenge 33](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/intersect/python/docs/hashtable_left_join)
- [Code Challenge 34](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/graph/python/docs/graph)
- [Code Challenge 37](https://github.com/MonikaChris/data-structures-and-algorithms-401-1/tree/trip/python/docs/graph_business_trip)

### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")
  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`
