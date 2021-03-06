

def valenceparameter_read(type, parameter):
    """Assigns values to the angle parameters part of the force field file."""
    
    try:
        file = open("ffield","r+")
        position = file.read().find("Nr of angles")
        file.seek(position)
        file.readline()
        position = file.tell()

        try:
            
            position = position + (73*(type-1))
            position = position + 10
            position = position + (parameter-1)*9
            
            file.seek(position)
            value=file.read(8)
    
        finally:
            file.close()
    except IOError:
        pass
        
    return value
