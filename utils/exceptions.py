
class Error(Exception):
	pass
	
	
class JSON_RPC_ERROR(Error):
	
	def __init__(self, data):
		self.error_code = data["error"]["code"]
		self.error_message = data["error"]["message"]
		super().__init__(self.error_message)
		
	def __str__(self):
		return f"{self.error_code} -> {self.error_message}"
		
