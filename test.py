from constants import MODE, MODEL_PATHS


from utilities import format_data, make_prediction


data = {'Group Name': "NIWA_Kit Basic_Location-Vente_Burkina-Faso_Afrique de l'Ouest",
  'Upfront Price': 20000,
  'Unlock Price': 124400,
  'Customer Gender': 'FEMALE',
  'Customer Age': 27,
  'Customer Occupation': 'Commerce',
  'Langue': 'Francais',
  'Region': 'CENTRE'}

da = {'Group Name': "NIWA_Kit Basic_Location-Vente_Burkina-Faso_Afrique de l'Ouest", 
        'Upfront Price': 20000.0, 
        'Unlock Price': 124400.0, 
        'Customer Gender': 'FEMALE', 
        'Customer Age': 27, 
        'Customer Occupation': 'Commerce', 
        'Langue': 'Francais', 
        'Region': 'CENTRE'}

d = {
       "groupname": "NIWA_Kit Basic_Location-Vente_Burkina-Faso_Afrique de l'Ouest",
       "upfront": 20000,
       "unlock": 124400,
       "gender": "FEMALE",
       "age": 27,
       "occupation": "Commerce",
       "langue": "Francais",
       "region": "CENTRE"
    }


mp = MODEL_PATHS[MODE]


v = make_prediction(mp,data)

print(v)