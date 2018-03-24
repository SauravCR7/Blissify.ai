'''
import requests
r = requests.post(
    "https://api.deepai.org/api/fast-style-transfer",
    data={
        'image': 'Saurav.jpg',
        'style': 'YOUR_STYLE_CHOICE',
    },
    headers={'api-key': 'e7b99044-d936-4112-8649-4bd0781ecbbe'}
)
print(r.json())
'''

# Example posting a local image file:
#e7b99044-d936-4112-8649-4bd0781ecbbe
import requests
r = requests.post(
    "https://api.deepai.org/api/fast-style-transfer",
    files={
        'image': open('frame.jpeg', 'rb'),
        'style': 'wave.ckpt',
    },
    headers={'api-key': 'e7b99044-d936-4112-8649-4bd0781ecbbe'}
)
print(r.json())

