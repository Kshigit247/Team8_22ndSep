class Main:
    def __init__(self):
        pass

    def run(self):
        print("Welcome to the Restaurant Recommendation System!")
        location = input("Enter your city: ")
        cuisines = input("Enter preferred cuisines (comma-separated): ").split(",")
        print(f"Location: {location}")
        print(f"Cuisines: {[c.strip() for c in cuisines]}")

if __name__ == "__main__":
    app = Main()
    app.run()
