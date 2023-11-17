from flask import Flask, request, jsonify
import urllib.parse, os, requests, json
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

from database_config import Config

token = os.environ['TOKEN']
port_number = int(os.environ['PORT'])
host_name = os.environ['HOST']

app = Flask(__name__)

@app.route('/vinyls', methods=['GET'])
def get_vinyls():
    try:

        artist_searched = request.get_json(silent=True)

        if not artist_searched:
            return jsonify({"message": "Invalid request: JSON is missing or incorrectly formatted"}), 400
        
        artist = urllib.parse.quote(artist_searched.get('artist'))
        url= f'https://api.discogs.com/database/search?artist={artist}&format=LP&per_page=90000'
        headers= {'Authorization': f'Discogs token={token}'}
        
        response = requests.get(url, headers=headers)
        data_received = response.json()

        results_pages = data_received['pagination']['pages']

        if results_pages > 1:
            data = []
            for page_number in range(1, results_pages +1):
                url = f'https://api.discogs.com/database/search?artist={artist}&format=LP&per_page=1000&page={page_number}'
                response = requests.get(url, headers=headers)
                data_received = response.json()
                results_on_page = data_received['results']
                data.extend(results_on_page)
        else:
            data = data_received.get('results')

        def save_to_database(artist_name, data_list):
            try:
                db = Config.get_database()
                collection = db['vinyl_collection'] 

                new_document ={
                    'artist_name': artist_name,
                    'vinyl_list': data_list
                } 

                result = collection.insert_one(new_document)
                return result               
               
            except Exception as e:
                print(e)
                return jsonify({'error': 'Internal Server Error'}), 500

    
        vinyl_list=[]
        for album in data:
            album_data = {
                'id':album['id'],
                'title': album['title'],
                'label': album['label'],
                'country': album['country'],
                'year': album['year'] if album.get('year') is not None else None,
                'format': album['format']           
            }
    
            vinyl_list.append(album_data)
        
    
        if not vinyl_list:
            return jsonify({'message': 'No vinyl records found by the artist you searched for'}), 404
        
        if request.args.get('save') == 'db':
            
            result = save_to_database(artist_searched.get('artist'), vinyl_list)
            if result:
                return jsonify({'message': 'vinyl list successfully saved to database'}), 201
            else:
                return jsonify({'error': 'Failed to save vinyl list to database'}), 500

        return jsonify(vinyl_list)
    
    except Exception as e:
        print('Exception: ', e)
        return jsonify({'error': 'Internal Server Error'}), 500 
   
       

@app.route('/minibio', methods=['GET'])
def get_minibio():
    try:
        
        data = request.get_json(silent=True)

        if not data:
            return jsonify({"message": "Invalid request: JSON is missing or incorrectly formatted"}), 400

        artist = urllib.parse.quote(data.get('artist'))
        url= f'https://en.wikipedia.org/wiki/{artist}'

        response = requests.get(url)


        occupations = [
        "Singer",
        "Songwriter",
        "Musician",
        "Actor",
        "Actress",
        "Painter",
        "Sculptor",
        "Record producer",
        "Music theorist",
        "Visual artist",
        "Writer",
        "filmmaker",
        "Multi-instrumentalist",
        "Composer",
        "Bandleader",
        "Pianist",
        "Arranger",
        "Artist",
        "Singer-songwriter",
        "Dancer"]

        def clean_html_tags(text, occupations):
            soup = BeautifulSoup(text, 'html.parser')
            cleaned_text = ' '.join(soup.stripped_strings)
            found_occupations = [occupation for occupation in occupations if occupation.lower() in cleaned_text.lower()]
            return found_occupations
        
        def save_to_database(data):
            try:
                db = Config.get_database()
                collection = db['minibio_collection']  
                data_with_string_keys = {str(key): value for key, value in data.items()}
                result = collection.insert_one(data_with_string_keys)                
               
            except:
                return jsonify({'error': 'Internal Server Error'}), 500
            

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', {'class': 'infobox'})
            if table:
                html_string = str(table)
                html_io = StringIO(html_string)
                date = pd.read_html(html_io, header=0, index_col=0)[0]
                minibio = date.transpose()
                columns_list =  list(minibio.columns)
                minibio.dropna(axis=1, how='all', inplace=True)

                minibio = minibio.reset_index(drop=True)
                minibio = minibio.assign(Name=[data])

                minibio.set_index('Name', inplace=True)
                minibio.reset_index(drop=True, inplace=True)


                search_term= '.* in .*'
                columns_to_remove = minibio.filter(regex=search_term, axis=1).columns
                minibio = minibio.drop(columns_to_remove, axis=1)


                if 'Occupations' in columns_list:
                    found_occupations = clean_html_tags(str(minibio['Occupations'].iloc[0]), occupations)

                    if found_occupations:
                        minibio['Occupations'] = [found_occupations]




                if 'Signature' in columns_list:
                    minibio=minibio.drop('Signature', axis=1)

                if 'Background information' in columns_list:
                    minibio = minibio.drop('Background information', axis=1)


        
                
                minibio_dict = minibio.to_dict(orient='index')

                if request.args.get('save') == 'db':
                    save_to_database(minibio_dict)
                    return jsonify({'message': 'Minibio successfully saved to database'}), 201
                

                return jsonify(minibio_dict)
            
        elif response.status_code == 404: 
            return jsonify({'error': 'Artist not found'}), 404
        
        else:
            return jsonify({'error': 'Internal Server Error'}), 500

    except:
        return jsonify({'error': 'Internal Server Error'}), 500        



app.run(port=port_number, host=host_name, debug=True)

