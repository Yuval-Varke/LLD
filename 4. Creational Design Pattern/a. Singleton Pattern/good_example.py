class Logger:
    # Class Variable
    __instance = None

    def __new__(cls, file_name: str):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
            cls.__instance.file_name = file_name # type: ignore
            cls.__instance.log_count = 0
            return cls.__instance
        else:
            return cls.__instance

    def log(self, msg):
        print(f"Logging {msg} in {self.file_name}") # type: ignore
        self.log_count += 1

    def get_log_count(self) -> int:
        return self.log_count


log1 = Logger("app.log")
log1.log("Hey")

log2 = Logger("app.log")
log2.log("Bye")

log3 = Logger("app.log")
log3.log("Good")

print(log1.get_log_count())
print(log2.get_log_count())
print(log3.get_log_count())