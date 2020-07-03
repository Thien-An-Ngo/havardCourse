class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

separation = "______________"

def main():

    # Create flight.
    f = Flight(origin="New York", destination="Paris", duration=540)

    # Print details about flight.
    print(f.origin)
    print(f.destination)
    print(f.duration)
    print(separation)
    # Change the value of a variable.
    f.duration += 10

    # Print details about flight again, viewing the change.
    print("is changed to")
    print(separation)
    print(f.origin)
    print(f.destination)
    print(f.duration)

if __name__ == "__main__":
    main()