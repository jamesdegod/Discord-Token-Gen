import random
import time
import base64

with open("tokens.txt", "a") as tokens:
  def genPart(l):
    userId=""
    for i in range(0, l):
      userId += str(random.randint(0, 9))
    return base64.b64encode(userId.encode()).decode().replace("=", "")

  def getToken():
    return f"{genPart(random.randint(17, 18))}.{genPart(4)}.{genPart(20)}"

  for i in range(0, 1000000000):
    token = getToken()
    tokens.write(token + "\n")
    print(token)
