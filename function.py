from bs4 import BeautifulSoup
import requests

def Execute(URL_BASE):
    
    processed_text='' 
    processed_text_trim=[]
    my_dict=dict()
    
    response = requests.get(URL_BASE,verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    meta = soup.find_all('meta')
    
    for tag in meta: #sprawdzanie metadanych pod kątem słów kluczowych
            if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['keywords']:
                processed_text=tag.attrs['content']
                
    processed_text=processed_text.lower() #ujednolicenie
    print(processed_text)
        
    if len(processed_text)>0: #sprawdzenie czy są jakies słowa kluczowe
        processed_text=processed_text.split(',') #rozdzielenie słów kluczowych 
        
        [processed_text_trim.append(i.strip()) for i in processed_text]
    
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        visible_text = soup.getText().lower() #wyodrębnienie tekstu strony głównej
       
        
        for i in range(0,len(processed_text_trim)):
            if processed_text_trim[i]!='': #szukanie i zliczanie słów kluczowych
                my_dict.update({processed_text_trim[i] : visible_text.count(processed_text_trim[i])}) 
            
    return my_dict
