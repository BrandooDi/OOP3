class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def change_fields(self, new_first, new_second):
        self.first = new_first
        self.second = new_second

    def compare_pairs(self, other_pair):
        if self.first > other_pair.first or (
            self.first == other_pair.first and self.second > other_pair.second
        ):
            return f"Pair {self} is greater than Pair {other_pair}"
        else:
            return f"Pair {self} is not greater than Pair {other_pair}"

    def __str__(self):
        return f"({self.first}, {self.second})"


class Fraction(Pair):
    def __init__(self, integer_part, fractional_part):
        super().__init__(integer_part, fractional_part)

    def compare_fractions(self, other_fraction):
        # Implement comparison logic for fractions here
        pass


if __name__ == "__main__":
    # Example demonstrating Pair class
    pair1 = Pair(3, 5)
    pair2 = Pair(2, 7)

    print(f"Pair 1: {pair1}")
    print(f"Pair 2: {pair2}")

    pair1.change_fields(4, 6)
    print(f"Pair 1 after change: {pair1}")

    comparison_result = pair1.compare_pairs(pair2)
    print(comparison_result)

    # Example demonstrating Fraction class
    fraction1 = Fraction(1, 0.5)
    fraction2 = Fraction(2, 0.3)

    print(f"Fraction 1: {fraction1}")
    print(f"Fraction 2: {fraction2}")

    fraction1.change_fields(3, 0.8)
    print(f"Fraction 1 after change: {fraction1}")

    fraction_comparison_result = fraction1.compare_fractions(fraction2)
    print(fraction_comparison_result)
