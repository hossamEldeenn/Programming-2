class FileManger:
    def __init__(self,file_name):
        self.file_name = file_name
        
    def read(self):
        return f'Read {self.file_name}'
    
    def write(self,content):
        return f'write {content} on {self.file_name}'
    
    
class CompressFiles:
    def __init__(self,file_name):
        self.file_name = file_name
        
    def compress(self):
        return f'{self.file_name} was compressed'
    
    def decompress(self):
        return f'{self.file_name} was decompressed'
    