import uuid

class UUIDManager:
    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())

    @staticmethod
    def is_valid_uuid(uuid_str):
        try:
            uuid.UUID(uuid_str)
            return True
        except ValueError:
            return False

    @staticmethod
    def get_version(uuid_str):
        try:
            uuid_obj = uuid.UUID(uuid_str)
            return uuid_obj.version
        except ValueError:
            return None

    @staticmethod
    def get_variant(uuid_str):
        try:
            uuid_obj = uuid.UUID(uuid_str)
            return uuid_obj.variant
        except ValueError:
            return None