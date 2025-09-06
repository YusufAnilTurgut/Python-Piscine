def NULL_not_found(object: any) -> int:
	if object is None:
		print("Nothing: None <class 'NoneType'>")
		return 0

	if isinstance(object, float) and object != object:
		print("Cheese: nan <class 'float'>")
		return 0
	
	if isinstance(object, bool) and object is False:
		print("Fake: False <class 'bool'>")
		return 0

	if isinstance(object, int) and object == 0:
		print("Zero: 0 <class 'int'>")
		return 0

    
	if isinstance(object, str) and object == "":
		print("Empty: <class 'str'>")
		return 0
		
	print("Type not Found")
	return 1