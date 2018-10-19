import random
import string
mchr = string.ascii_letters + string.digits
# mchr = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print({''.join(random.sample(mchr, 6)) for i in range(200)})
print({''.join(random.choice(mchr) for j in range(6))for i in range(200)})