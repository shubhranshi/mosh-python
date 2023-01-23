# Sometimes we need to create our own custom type containers (or data structure)
# Container are data structure like lists, dictionary tuples and so on.

# We are going to create a custom container type
# In this example we are going to keep track of the several tag on a blog.

# We want to this container class to support various operations like
# getting the number of items in the container, get the item by its key
# set the items, iterate over the container, so on.

class TagCloud:

    def __init__(self):     # For this example we are going to use a dictionary
        self.tags = {}      # We are initializing an empty dictionary

    # Implementing a method to add tags to the dictionary.
    # If the tag exits it will be incremented by one.
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # Implementing a magic method to get the value of a tag,
    # if that tag does not exist it will return 0
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # Implementing a magic method to set the value for a certain key, in our case tag
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # Implementing a magic method to get the number of tags
    def __len__(self):
        return len(self.tags)

    # Implementing a magic method to make our object iterable
    def __iter__(self):
        return iter(self.tags)  # iter functions returns iterable object


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
# a typical dictionary will treat 'python' 'Python' as 2 different keys.
# Using a custom class, we can add more features and customize it,
# at the same time these customization will be encapsulated in this custom class.
cloud.add("Python")
cloud.add("JavaScript")
print(cloud.tags)

# in order to read the count of a tag, we need to implement a magic method __getitem__
print(cloud["python"])

# in order to set the count of a tag, we need to implement a magic method __setitem__
cloud["Javascript"] = 10
cloud["C++"] = 5

print(cloud.tags)

# in order to get the number of items in the tag cloud, we need to implement magic method __len__
print(len(cloud))

# in order to make it iterable, we need to implement magic method __iter__
for tag in cloud:
    print(tag)

for tag, count in cloud.tags.items():
    print(tag, count)

for tag in cloud:
    print(tag, cloud[tag])