blockchain_storage = {}

def add_record(file_hash, owner):
    import datetime
    record = {
        'hash': file_hash,
        'owner': owner,
        'timestamp': str(datetime.date.today())
    }
    blockchain_storage[file_hash] = record
    return record
