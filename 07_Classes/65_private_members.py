# In python, we can define an attribute as private by prefixing it with '__'.
# However, this is more of a conventional practice, we can still access the private variables
# by using ".__dict__"

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()

cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("Python")
cloud.add("JavaScript")
cloud.add("JAVASCRIPT")

print(cloud["PYTHON"])
# We get the value for the tag Python that it is 4

# print(cloud.tags["PYTHON"])

# Here we get an error AttributeError: 'TagCloud' object has no attribute 'tags'
# because we are accessing the underling dictionary of the class
# and there we do not have the "PYTHON" tag with capital letters
# To fix we need to hide this attribute from the outside of the class by
# prefixing it with 2 underscores "__tags"

print(cloud.__dict__)