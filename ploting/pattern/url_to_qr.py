import qrcode

def url_to_qr(src):
    qr = qrcode.make(src)
    qr.save("qr.png")
    print("qr generated successfully")


s ="https://github.com/Aashishbirhade/interview-preparation-challenges"
url_to_qr(s)