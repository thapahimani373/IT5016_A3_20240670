from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method – forces kids to define area, hides details.

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  # Hides the math inside.

# Analysis: Abstraction simplifies things – users just call area() without knowing how. It’s maintainable because I can add Square later without changing old code. I didn’t get it at first, but now I see it’s like a magic button!
circle = Circle(5)
print(f"Circle area: {circle.area()}")
