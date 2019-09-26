def almost_there(n):
   return (abs(100 -n) <= 10) or (abs(200 -n) <= 200)


print(almost_there(500))