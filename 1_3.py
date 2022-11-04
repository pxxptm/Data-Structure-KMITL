
print("*** Reading E-Book ***")

inputText , highlightText = input("Text , Highlight : ").split(",")

replaceText = "[" + highlightText + "]"

print(inputText.replace(highlightText,replaceText))
