import requests
import csv

#url to download the data
url = "https://data.nasa.gov/resource/y77d-th95.json"
# Specify the output file name
output_csv = "nasa_data.csv"

def download_data(url):
    # Get the data from the url
    response = requests.get(url)
    #extract the response data from json and store it in variable data
    data = response.json()
    return data

def save_as_csv(data,output_csv):

    fieldnames = ['name', 'id', 'nametype', 'recclass', 'mass', 'year', 'reclat', 'reclong', 'coordinates']

    with open (output_csv,'w',newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        # write the header in the output csv file
        writer.writeheader()
        #fetch the row data and store it in output csv
        for row in data:
            # Extract the desired attributes from the row
            name = row.get('name')
            id = row.get('id')
            nametype = row.get('nametype')
            recclass = row.get('recclass')
            mass = row.get('mass (g)')
            year = row.get('year')
            reclat = row.get('reclat')
            reclong = row.get('reclong')
            coordinates = [row.get('reclat'), row.get('reclong')]

            # Write the extracted attributes to the CSV file
            writer.writerow({
                'name': name,
                'id': id,
                'nametype': nametype,
                'recclass': recclass,
                'mass': mass,
                'year': year,
                'reclat': reclat,
                'reclong': reclong,
                'coordinates': coordinates
            })

    print(f"Downloaded Data and Successfully stored in csv: {output_csv}")

# download the data    
data = download_data(url)
# Convert and save the data as CSV
save_as_csv(data,output_csv)

