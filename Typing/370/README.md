In this Bite, you have to add type hints to all methods of the Vector class. Here are a few marks:

- When you need the type of the class itself, you can use a quoted type, see Forward references. There are other possibilities (for example Self with 3.11), but we are just getting started, aren't we.

- The Vector class will work both with integers and floats. Does that mean you always have to annotate both types? You don't, thanks to the numeric tower. In short: Although int is not a subclass of float, the type float also accepts the type int. So just stick with float for now.

- Please annotate all methods, dunder methods included.

- The dunder method __mul__ can return two different things, depending on the passed attribute's type. You will learn about a better way to do this, but for now, stick with typing.Union.