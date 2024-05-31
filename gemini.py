import google.generativeai as genai




# Configure the API with your API key
genai.configure(api_key=google_api_key)

model = genai.GenerativeModel('gemini-pro')
# model = genai.GenerativeModel('gemini-pro-vision')
def gemin (vari): 
    response = model.generate_content(vari)
    # print(response)
    re=response.text
    l2=re.replace("*","")
    # print(l2)
    return l2
# print(gemin("what is an LLM "))