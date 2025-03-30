import tkinter as tk
from core.encryption import HomomorphicEncryption
from core.text_encryption import TextHomomorphicEncryption
from ui.app import HomomorphicEncryptionApp


def main():
    # Generate global encryption instances with predefined parameters
    numeric_encryption = HomomorphicEncryption(p=17, g=3)
    # Generate keys during initialization
    numeric_encryption.generate_key()

    text_encryption = TextHomomorphicEncryption(p=17, g=3)
    # Text encryption will use the same numeric encryption instance

    app = HomomorphicEncryptionApp(numeric_encryption, text_encryption)
    app.mainloop()


if __name__ == "__main__":
    main()