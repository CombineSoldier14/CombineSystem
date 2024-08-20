import cowsay

def cowsaycmd():
    text = input("What should the cow say?: ")
    return cowsay.cow(text)