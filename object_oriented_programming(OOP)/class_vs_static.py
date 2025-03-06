# CLASS METHOD vs STATIC METHOD

# when to use static method.
class Item:
    @staticmethod
    def when_static():
        '''
        1. we will use a static method when we want to do something that should not be unique per instance.

        2. this should do something that has a relationship with the class, but not something that must be unique per instance.
        '''

# when to use class method.
    
    
    @classmethod
    def when_class(cls):
        '''
        1.we create class methods for instantiating instances from some structured data that i own. those are used to manipulate different structures of data to instantiate objects. that is why the class method should be existing in any class, especially if i have to instantiate hundreds of objects on my program. 

        2. this should also do something that has a relationship with the class, but usually those are used to manipulate different structures of data to instantiate objects, like we have done with csv.
        '''


# the main difference between these mehods is that, the static method are not passing the object reference as the first argument in the background. static and class can not only be called from the class level but also can be called from the instances. but there is no reason to call those methods from instances .