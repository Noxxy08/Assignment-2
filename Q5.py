from abc import ABC , abstractmethod

class FileHandler(ABC):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """Read content from the file. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def write(self, data):
        """Write content to the file. Must be implemented by subclasses."""

    def describe(self):
        print(f"Handling file: {self.filename}")

class TextFileHandler(FileHandler):
    def read(self):
        try:
            with open(self.filename, "r") as f:
                content = f.read()
                print(f"[Text] Read content:\n{content}")
                return content
        except FileNotFoundError:
            print(f"Error: '{self.filename}' not found.")
            return None

    def write(self, data):
        with open(self.filename, "w") as f:
            f.write(data)
        print(f"[Text] Wrote data to '{self.filename}'.")

class BinaryFileHandler(FileHandler):
    def read(self):
        try:
            with open(self.filename, "rb") as f:
                content = f.read()
                print(f"[Binary] Read {len(content)} bytes.")
                return content
        except FileNotFoundError:
            print(f"Error: '{self.filename}' not found.")
            return None

    def write(self, data):
        with open(self.filename, "wb") as f:
            f.write(data)
        print(f"[Binary] Wrote {len(data)} bytes to '{self.filename}'.")


text_handler = TextFileHandler("sample.txt")
text_handler.describe()
text_handler.write("Hello, this is my modified text file.")
text_handler.read()

print()

binary_handler = BinaryFileHandler("sample.bin")
binary_handler.describe()
binary_handler.write(b"\x00\x01\x02\x03\x04")
binary_handler.read()

print()

try:
    handler = FileHandler("test.txt")
except TypeError as e:
    print(f"Error: {e}")