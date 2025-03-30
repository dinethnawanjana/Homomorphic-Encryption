import base64


class EncryptionConverter:
    @staticmethod
    def encrypt_to_base64(encrypted_data):
        """
        Convert encrypted data to base64 string for storage/transmission
        """
        # Convert tuple to bytes
        data_bytes = str(encrypted_data).encode('utf-8')
        return base64.b64encode(data_bytes).decode('utf-8')

    @staticmethod
    def base64_to_encrypt(base64_str):
        """
        Convert base64 string back to encrypted data
        """
        decoded_bytes = base64.b64decode(base64_str)
        return eval(decoded_bytes.decode('utf-8'))
