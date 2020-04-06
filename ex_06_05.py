text = "X-DSPAM-Confidence:    0.8475"
findtext = text.find('0.8475')
piece = text[findtext:]
host = float(piece)
print(host)
