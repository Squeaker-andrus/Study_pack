print(b'r\xc3\xa9sum\xc3\xa9'.decode("utf-8"))
print(b'r\xc3\xa9sum\xc3\xa9'.decode("utf-8").encode("Latin1"))
print(b'r\xc3\xa9sum\xc3\xa9'.decode("utf-8").encode("Latin1").decode("Latin1"))
