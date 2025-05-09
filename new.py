import phonenumbers
from phonenumbers import geocoder
import folium
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
import json

def print_location_details(results):
    if results and len(results) > 0:
        result = results[0]
        print("\n=== Location Details ===")
        print(f"Formatted Address: {result['formatted']}")
        
        components = result['components']
        print("\nAdministrative Details:")
        print(f"Country: {components.get('country', 'N/A')}")
        print(f"State: {components.get('state', 'N/A')}")
        print(f"City: {components.get('city', 'N/A')}")
        print(f"Postcode: {components.get('postcode', 'N/A')}")
        print(f"Road: {components.get('road', 'N/A')}")
        print(f"House Number: {components.get('house_number', 'N/A')}")
        
        print("\nGeographic Information:")
        print(f"Continent: {components.get('continent', 'N/A')}")
        print(f"Country Code: {components.get('country_code', 'N/A').upper()}")
        
        if 'bounds' in result:
            bounds = result['bounds']
            print("\nBounding Box:")
            print(f"Northeast: {bounds['northeast']['lat']}, {bounds['northeast']['lng']}")
            print(f"Southwest: {bounds['southwest']['lat']}, {bounds['southwest']['lng']}")
        
        print(f"\nConfidence Score: {result.get('confidence', 'N/A')}/10")

def create_enhanced_map(lat, lng, location_name, results):
    map_location = folium.Map(location=[lat, lng], zoom_start=12)
    
    # Add main marker with popup
    folium.Marker(
        [lat, lng],
        popup=folium.Popup(location_name, max_width=300),
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(map_location)
    
    # Add circle to show approximate area
    folium.Circle(
        radius=1000,  # 1km radius
        location=[lat, lng],
        color='blue',
        fill=True,
        popup='Approximate Area'
    ).add_to(map_location)
    
    if results and len(results) > 0 and 'bounds' in results[0]:
        bounds = results[0]['bounds']
        # Add rectangle to show bounds
        folium.Rectangle(
            bounds=[[bounds['southwest']['lat'], bounds['southwest']['lng']],
                   [bounds['northeast']['lat'], bounds['northeast']['lng']]],
            color='green',
            fill=True,
            popup='Location Bounds'
        ).add_to(map_location)
    
    return map_location

def main():
    key = "2f92da82d2164970a0b250df0098414f"
    
    print("Phone Number Location Tracker")
    print("============================")
    
    number = input("Enter phone number with country code (e.g., +254123456789): ")
    
    try:
        # Parse phone number
        check_number = phonenumbers.parse(number)
        
        # Get country location
        number_location = geocoder.description_for_number(check_number, "en")
        print(f"\nCountry Location: {number_location}")
        
        # Get carrier information
        service_provider = phonenumbers.parse(number)
        carrier_name = carrier.name_for_number(service_provider, "en")
        print(f"Service Provider: {carrier_name}")
        
        # Get detailed location information using OpenCage
        opencage_geocoder = OpenCageGeocode(key)
        query = str(number_location)
        results = opencage_geocoder.geocode(query)
        
        if results and len(results) > 0:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            print(f"Coordinates: {lat}, {lng}")
            
            # Print detailed location information
            print_location_details(results)
            
            # Create enhanced map
            map_location = create_enhanced_map(lat, lng, number_location, results)
            map_location.save("mylocation.html")
            print("\nMap has been saved as 'mylocation.html'")
            
        else:
            print("No detailed location information found")
            
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Error: Invalid phone number format. Please include the country code (e.g., +254123456789)")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()